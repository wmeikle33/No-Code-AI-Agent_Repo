from workflows.workflow_state import WorkflowState
from workflows.router import route_request
from workflows.workflow_registry import get_agent
from workflows.tool_runner import run_tool
from workflows.human_review import check_human_review
from workflows.error_handling import format_error


def run_workflow(user_request: str) -> dict:
    state = WorkflowState(user_request=user_request)

    try:
        agent_name = route_request(user_request)
        state.selected_agent = agent_name

        agent_config = get_agent(agent_name)

        for tool_name in agent_config["tools"]:
            state.tool_outputs[tool_name] = run_tool(tool_name, user_request)

        state.final_output = {
            "status": "success",
            "agent": state.selected_agent,
            "answer": f"Handled by {state.selected_agent}.",
            "tool_outputs": state.tool_outputs
        }

        state.requires_human_review = check_human_review(
            user_request,
            state.final_output
        )

        state.final_output["requires_human_review"] = state.requires_human_review

        return state.final_output

    except Exception as error:
        state.errors.append(str(error))
        return format_error(error)
