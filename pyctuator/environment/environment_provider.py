from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing import Mapping, Optional, List


@dataclass
class PropertyValue:
    value: str
    origin: Optional[str] = None


@dataclass
class PropertiesSource:
    name: str
    properties: Mapping[str, PropertyValue]


@dataclass
class EnvironmentData:
    activeProfiles: List[str]
    propertySources: List[PropertiesSource]


class EnvironmentProvider(ABC):

    @abstractmethod
    def get_properties_source(self) -> PropertiesSource:
        pass
