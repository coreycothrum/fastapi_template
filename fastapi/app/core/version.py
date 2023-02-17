from semver import Version


class PydanticVersion(Version):
    @classmethod
    def _parse(cls, version):
        return cls.parse(version)

    @classmethod
    def __get_validators__(cls):
        yield cls._parse

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update()
