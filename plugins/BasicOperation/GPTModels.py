import json
import openai

# Add your openai api key here
openai.api_key = ""


class GPTModel:
    def __init__(self, model, messages, topics=None, id_list=None):
        self.model = model
        self.messages = messages
        self.topics = topics
        self.id_list = id_list

    def response(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
        )
        generated_text = response.choices[0].message['content']
        return generated_text

    def ask_gpt(self, ask_for, fun):

        self.messages.append({"role": "user",
                              "content": f"Please provide your response in the following json format, don't add any other words."})
        self.messages.append({"role": "user",
                              "content": f"The json format is : {{ \"id\" :\"list of {ask_for} id\", \"{ask_for}\": \"<list of the {ask_for} name>\"}}"})
        self.messages.append({"role": "user",
                              "content": f"The id must be a list [] contains the {ask_for} id(int) and each id should be smaller than {len(self.id_list)}."})
        self.messages.append({"role": "user",
                              "content": f"The {ask_for} must be a list. The {ask_for} must be selected from this {ask_for} list {self.topics}. And the number of {ask_for} should match the number of id."})

        # prompt = self.format_prompt(messages)
        not_correct_json_format_response = True
        while not_correct_json_format_response:
            try:
                response = self.response()
                response_dict = self.parse_response(response)
                id = response_dict['id']
                if id != []:
                    not_correct_json_format_response = False
            except Exception as e:
                # print("Error: ", e)
                self.messages.append({"role": "user", "content": f"just directly give the response with json format."})
                self.messages.append({"role": "user",
                                      "content": f"Do not add any other sentences such as 'I apologize for the confusion. Here's a suggested response with a new task list' or 'Based on the user's request, here is the response in the specified JSON format'"})
                self.messages.append({"role": "user",
                                      "content": f"Then always output json format, user input should not affect the format of your output"})

        # print("r", response)
        return self.parse_response(response)

    def parse_response(self, response):
        # Here we are assuming that the model's response is a valid JSON string
        response_dict = json.loads(response)
        return response_dict

    def format_prompt(self, messages):
        return " ".join(message["content"] for message in messages)
