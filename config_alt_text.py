APP_TITLE = "Alt Text Generator"
APP_INTRO = """This app accepts images via upload or URL and returns alt text for accessibility."""

APP_HOW_IT_WORKS = """
This app creates alt text for accessibility from images. 
                For most images, it provides brief alt text to describe the image, focusing on the most important information first. 

                For complex images, like charts and graphs, the app creates a short description of the image and a longer detail that describes what the complex image is conveying. 

                For more information, see <a href="https://www.w3.org/WAI/tutorials/images/" target="_blank">W3C Images Accessibility Guidelines</a>
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You accept images in url and file format to generate description or alt text according to WCAG and ADA standards."""

PHASES = {
    "phase1": {
        "name": "Image Input and Alt Text Generation",
        "fields": {
            "http_img_urls": {
                "type": "text_area",
                "label": "Enter image urls"
            },
            "uploaded_files": {
                "type": "file_uploader",
                "label": "Choose files",
                "allowed_files": ['png', 'jpeg', 'gif', 'webp'],
                "multiple_files": True,
            },
            "important_text": {
                "type": "checkbox",
                "label": "The text in my image(s) is important",
                "value": False,
                "help": "If text is important, it should be included in the alt text. If it is irrelevant or covered in text elsewhere on the page, it should not be included",
            },
            "complex_image": {
                "type": "checkbox",
                "label": "My image is a complex image (chart, infographic, etc...)",
                "value": True,
                "help": "Complex images get both a short and a long description of the image",
            }
        },
        "phase_instructions": "Generate the alt text for the image urls and uploads",
        "user_prompt": "",
        "show_prompt": True,
        "allow_skip": False
    }
}

# Function to handle prompt conditionals based on checkbox values
def prompt_conditionals(prompt,user_input, phase_name=None):
    if 'complex_image' in user_input and user_input['complex_image']:
        conditional_prompt = """I am sending you one or more complex images. Please provide a short description to identify the image, and a long description to represent the essential information conveyed by the image. \n
        Please provide your output in this format \n
        **Short Description:**\n
        [Short Description]\n\n
        **Long Description:**\n
        [Long Description]"""
    else:
        conditional_prompt = """I am sending you one or more images. Please provide separate appropriate alt text for each image I send. The alt text should:
        - Aim to put the most important information at the beginning. \n"""
        if 'important_text' in user_input and user_input['important_text']:
            conditional_prompt += """- Make sure to include any text in this image as part of the alt text"""
    prompt = "Here is the uploaded images - {http_img_urls} and {uploaded_files}"
    return conditional_prompt+"\n"+prompt

selected_llm = "gpt-4o-mini"


LLM_CONFIGURATIONS = {
    "gpt-4o-mini": {
        "model": "gpt-4o-mini",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.150,
        "price_output_token_1M":.600
    },
    "gpt-4-turbo": {
        "model": "gpt-4-turbo",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":10,
        "price_output_token_1M":30
    },
    "gpt-4o": {
        "model": "gpt-4o",
        "frequency_penalty": 0,
        "max_tokens": 250,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":5,
        "price_output_token_1M":15
    },
    "gemini-1.0-pro": {
        "model": "gemini-1.0-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.5,
        "price_output_token_1M":1.5
    },
    "gemini-1.5-flash": {
        "model": "gemini-1.5-flash",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.35,
        "price_output_token_1M":1.05
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":3.5,
        "price_output_token_1M":10.50
    },
    "claude-3.5-sonnet": {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-opus": {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 15,
        "price_output_token_1M": 75
    },
    "claude-sonnet": {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-haiku": {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 0.25,
        "price_output_token_1M": 1.25
    }
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thanks for using the Alt Text Generator service"
COMPLETION_CELEBRATION = False