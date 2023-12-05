from .assistants import Assistant


class PartyAssistant(Assistant):
    def __init__(self, model, description, instructions, metadata, name, tools):
        super().__init__(model=model, description=description, instructions=instructions, metadata=metadata, name=name, tools=tools)
        
    # Implement additional methods or functionality specific to the party assistant
    # ...
