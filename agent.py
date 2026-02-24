import os
import uuid
import asyncio
from datetime import datetime
import edge_tts
from deep_translator import GoogleTranslator

class SpeechAgent:
    def __init__(self):
        self.audio_dir = os.path.join('static', 'audio')
        if not os.path.exists(self.audio_dir):
            os.makedirs(self.audio_dir)
            
        # Neural Voice Mapping (Microsoft Edge TTS)
        # format: { 'lang_code': { 'Male': 'voice_id', 'Female': 'voice_id' } }
        self.voice_map = {
            'en': {'Male': 'en-US-GuyNeural', 'Female': 'en-US-AriaNeural'},
            'hi': {'Male': 'hi-IN-MadhurNeural', 'Female': 'hi-IN-SwaraNeural'},
            'te': {'Male': 'te-IN-MohanNeural', 'Female': 'te-IN-ShrutiNeural'},
            'ta': {'Male': 'ta-IN-ValluvarNeural', 'Female': 'ta-IN-PallaviNeural'},
            'kn': {'Male': 'kn-IN-GaganNeural', 'Female': 'kn-IN-SapnaNeural'},
            'ml': {'Male': 'ml-IN-MidhunNeural', 'Female': 'ml-IN-SobhanaNeural'},
            'bn': {'Male': 'bn-IN-BashkarNeural', 'Female': 'bn-IN-TanishaNeural'},
            'mr': {'Male': 'mr-IN-ManoharNeural', 'Female': 'mr-IN-AarohiNeural'},
            'gu': {'Male': 'gu-IN-NiranjanNeural', 'Female': 'gu-IN-DhwaniNeural'},
            'pa': {'Male': 'pa-IN-ArjunNeural', 'Female': 'pa-IN-VaaniNeural'},
            'ur': {'Male': 'ur-PK-AsadNeural', 'Female': 'ur-PK-UzmaNeural'},
            'or': {'Male': 'en-IN-PrabhatNeural', 'Female': 'en-IN-AnanyaNeural'} # Fallback to Indian English for Odia if not direct
        }

    def validate(self, text):
        if not text or not text.strip():
            return False, "Input text cannot be empty."
        if len(text) > 1000:
            return False, "Input text is too long (max 1000 characters)."
        return True, "Success"

    def decide_parameters(self, text):
        # Neural voices handle speed differently, we can adjust rate if needed
        rate = "+0%"
        if len(text) > 200:
            rate = "-10%" # Slightly slower for long text
        return {"rate": rate}

    async def generate_async(self, text, rate, voice):
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join(self.audio_dir, filename)
        
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(filepath)
        
        return f"/static/audio/{filename}"

    def run(self, text, lang='en', gender='Female'):
        # 1. Validate
        is_valid, message = self.validate(text)
        if not is_valid:
            return {
                "status": "error",
                "message": message,
                "audio_path": None,
                "timestamp": datetime.now().isoformat()
            }

        try:
            # 2. Translate if needed
            translated_text = text
            if lang != 'en':
                try:
                    translated_text = GoogleTranslator(source='auto', target=lang).translate(text)
                except Exception as te:
                    print(f"Translation error: {te}")
            
            # 3. Decide Parameters
            params = self.decide_parameters(translated_text)
            
            # 4. Select Voice
            voice_config = self.voice_map.get(lang, self.voice_map['en'])
            voice = voice_config.get(gender, voice_config['Female'])
            
            # 5. Generate (handling async in sync context)
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            audio_path = loop.run_until_complete(self.generate_async(translated_text, params['rate'], voice))
            loop.close()
            
            return {
                "status": "success",
                "message": f"Speech generated successfully in {lang} ({gender}).",
                "audio_path": audio_path,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"An error occurred: {str(e)}",
                "audio_path": None,
                "timestamp": datetime.now().isoformat()
            }
