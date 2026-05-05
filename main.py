from enum import Enum
from google import genai
class InstrumentEnum(Enum):
    PERCUSSION = 'Percussion'
    STRING = 'String'
    WOODWIND = 'Woodwind'
    BRASS = 'Brass'
    KEYBOARD = 'Keyboard'

client = genai.Client(api_key='AIzaSyAykFqA8rlHzR5fsVEzvPb_4zZCuIVLFf8')

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='What instrument plays multiple notes at once?',
    config={
        'response_mime_type': 'text/x.enum',
        'response_schema': InstrumentEnum,
    },
)
print(response.text)