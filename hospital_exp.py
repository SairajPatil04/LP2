class MedicalExpertSystem:
    def __init__(self):
        # Store possible conditions and their related symptoms
        self.conditions = {
            "Flu": ["fever", "cough", "fatigue", "sore throat", "runny nose"],
            "Cold": ["cough", "sore throat", "runny nose", "sneezing"],
            "Covid-19": ["fever", "cough", "shortness of breath", "loss of taste or smell"],
            "Allergy": ["sneezing", "runny nose", "itchy eyes", "cough"],
            "Stomach Flu": ["nausea", "vomiting", "diarrhea", "fever"]
        }

    def diagnose(self, symptoms):
        # Compare the symptoms with the conditions
        possible_conditions = []
        
        for condition, condition_symptoms in self.conditions.items():
            matching_symptoms = set(symptoms).intersection(set(condition_symptoms))
            if len(matching_symptoms) >= 2:  # If at least 2 symptoms match
                possible_conditions.append((condition, matching_symptoms))

        if possible_conditions:
            return possible_conditions
        else:
            return "No matching conditions found. Please consult a doctor."

    def start_chat(self):
        print("Medical Expert System: Hello, I can help diagnose basic conditions based on your symptoms.")
        print("Type 'exit' to end the conversation.")

        while True:
            # Ask the user for symptoms
            user_input = input("Please enter your symptoms (comma separated): ")

            if user_input.lower() == "exit":
                print("Goodbye! Stay healthy!")
                break

            # Convert the user input into a list of symptoms
            symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]

            # Get diagnosis
            result = self.diagnose(symptoms)

            # Display the result
            if isinstance(result, list):
                print("Possible Conditions based on your symptoms:")
                for condition, matching_symptoms in result:
                    print(f"- {condition} (Matching symptoms: {', '.join(matching_symptoms)})")
            else:
                print(result)

# Create an instance of the MedicalExpertSystem and start interaction
expert_system = MedicalExpertSystem()
expert_system.start_chat()
