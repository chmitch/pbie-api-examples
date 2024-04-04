#"{\"credentialData\":[{\"name\":\"username\", \"value\":\"john\"},{\"name\":\"password\", \"value\":\"*****\"}]}"

import dataclasses
from typing import List
from dataclasses import dataclass

@dataclass()
class NameVal:
    name: str
    val: str

#init=Fals to avoid the complex constructor requirement which lets us create an empty object and add items to the list
@dataclass(init=False)
class BasicCredential:
    credentialData: List[NameVal]

    def __init__(self):
        self.credentialData = []

