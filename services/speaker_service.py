from schemas.speaker import Speaker, SpeakerCreate

from database import speakers

class SpeakerService:

    @staticmethod
    def create_speaker(speaker_in: SpeakerCreate):
        new_id = max(speakers.keys(), default=0) + 1
        speaker = Speaker(id=new_id, **speaker_in.model_dump())
        speakers[new_id] = speaker
        return speaker
    
    @staticmethod
    def get_speaker_by_id(speaker_id: str):
        return speakers.get(speaker_id)
    
    @staticmethod
    def delete_speaker(speaker_id: str):
        if speaker_id not in speakers:
            return None
        del speakers[speaker_id]
        return True
    
speaker_service = SpeakerService()