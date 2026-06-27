
class AgentPlatformError(Exception):
    """Base exception for the platform."""


class WorkflowError(AgentPlatformError):
    """Workflow execution failed."""


class ValidationError(AgentPlatformError):
    """Input or output validation failed."""


class RoutingError(AgentPlatformError):
    """Agent routing failed."""


class ToolExecutionError(AgentPlatformError):
    """Tool execution failed."""


class ConfigurationError(AgentPlatformError):
    """Configuration is invalid."""


class ModelError(AgentPlatformError):
    """LLM/model call failed."""


class DatabaseError(AgentPlatformError):
    """Database operation failed."""
