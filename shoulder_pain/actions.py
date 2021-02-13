
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction




class SurveyForm(FormAction): 
 def name(self):
  return "survey_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["describe_pain","severe_pain", "increase_pain", "drop","sleeping","lifting","reaching_out","throwing","work","sport",
   "pain_arm", "pain_night", "clicking", "shoulder_weakness", "arm_weakness", "numbness", "stiffness", "neck",
  "other_symptoms"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "describe_pain": [
                self.from_text(),
            ],
            "severe_pain": [
                self.from_text(),
            ],
            
            "increase_pain": [
                self.from_text(),
            ],
            "drop": [
                self.from_text(),
            ],
            "sleeping": [
                self.from_text(),
            ],
            "lifting": [
                self.from_text(),
            ],
            "reaching_out": [
                self.from_text(),
            ],
            "throwing": [
                self.from_text(),
            ],
            "work": [
                self.from_text(),
            ],
            "sport": [
                self.from_text(),
            ],
            "pain_arm": [
                self.from_text(),
            ],
            "pain_night": [
                self.from_text(),
            ],
            "clicking": [
                self.from_text(),
            ],
            "shoulder_weakness": [
                self.from_text(),
            ],
            "arm_weakness": [
                self.from_text(),
            ],
            "numbness": [
                self.from_text(),
            ],
            "stiffness": [
                self.from_text(),
            ],
            "neck": [
                self.from_text(),
            ],
            "other_symptoms": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("Thank you for your patience")    
    return []
