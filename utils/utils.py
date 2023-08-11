from typing import Dict, Any
import configparser
import openai
import time


def load_openai_api_key(path: str = "credentials.ini", verbose: bool = False):
    """ Loads api key into openai lib allowing to send api requests in given session. """
    try:
        config = configparser.ConfigParser()
        config.read(path)

        openai.organization = config["openai"]["org"]
        openai.api_key = config["openai"]["api_key"]

        if verbose:
            print("Successfully loaded OpenAI api key.")
    except Exception as e:
        raise Exception(f"Failed to load openai api key config, with error: {e}")


# openai requets sent
def send_openai_chat_completion_request(
        prompt: str = None, 
        system_prompt: str = None, 
        temperature: float = 0.5, 
        retry=3,
        verbose: bool = False,
    ):
    """ Sends openai api completion request to obtain text generated for out prompt. Handles api unavailability. """
    if prompt==None:
        raise Exception("Trying to send an empty openai chat completion request.")
    
    res = None
    for _ in range(retry):
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
            )
        except Exception as e:
            if verbose:
                print(f"Failed to send openai chat completion request, with error: {e}")
            time.sleep(5) # repeating the request after cooldown period

        if res:
            break # got our result, no need to repeat the api call

    return res


# parse ai output
def parse_openai_chat_completion_res(res: Dict[str, Any] = None, verbose: bool = False):
    """ Reads the generative essence from api call response structure. """
    if not res:
        if verbose:
            print("Warning - trying to parse non-existent api call response.")
        return None # handled during result display
    
    generation = res["choices"][0]["message"]["content"]
    return generation


# create a calendar
# save data to file