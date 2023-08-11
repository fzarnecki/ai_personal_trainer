from typing import Dict, Any, Union
import configparser
import openai
import time
import json


def load_openai_api_key(path: str = "utils/credentials.ini", verbose: bool = False):
    """ Loads api key into openai lib allowing to send api requests in given session. """
    try:
        config = configparser.ConfigParser()
        config.read(path)

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
    ) -> Dict[str, Any]:
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


def parse_openai_chat_completion_res(res: Dict[str, Any] = None, verbose: bool = False) -> Union[None, str]:
    """ Reads the generative essence from api call response structure. """
    if not res:
        if verbose:
            print("Warning - trying to parse non-existent api call response.")
        return None # handled during result display
    
    generation = res["choices"][0]["message"]["content"]
    print(generation)
    if json.loads(generation):
        res_json = json.loads(generation)
        if isinstance(res_json, list):
            for elem in res_json:
                if not "day" in elem or not "content" in elem:
                    return None
            return res_json
    return None


def form_prompt_workout_plan_json(gathered_data: Dict[str, Any]):
    """ Based on data gathered from user, forms prompt to obtain workout plan generated by llm. """
    prompt = f"You are given a questionnaire filled with personal information, in a python doctionary form. Based on the data provided design a workout week (7 days) for the person. The return data should be structured as a list of json documents, each with day and content fields. The questionnaire is as follows: {json.dumps(gathered_data)}. Return only a list of json, nothing else."
    return prompt


def parse_openai_chat_completion_res_simple(res: Dict[str, Any] = None, verbose: bool = False) -> Union[None, str]:
    """ Reads the generative essence from api call response structure. """
    if not res:
        if verbose:
            print("Warning - trying to parse non-existent api call response.")
        return None # handled during result display
    
    generation = res["choices"][0]["message"]["content"]
    return generation


def form_prompt_workout_plan_simple(gathered_data: Dict[str, Any]):
    """ Based on data gathered from user, forms prompt to obtain workout plan generated by llm. """
    prompt = f"You are given a questionnaire filled with personal information, in a python doctionary form. Based on the data provided design a workout week (7 days) for the person. The questionnaire is as follows: {json.dumps(gathered_data)}."
    return prompt


# create a calendar

# save data to file