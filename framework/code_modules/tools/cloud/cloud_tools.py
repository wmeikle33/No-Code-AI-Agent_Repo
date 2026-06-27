from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


SUPPORTED_PROVIDERS = {"aws", "azure", "gcp"}


def load_cloud_config(config_path: str) -> Dict[str, Any]:
    """Load a cloud configuration JSON file."""
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_cloud_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate required fields for a cloud config."""
    required_fields = ["provider", "service", "region"]
    missing_fields = [field for field in required_fields if field not in config]

    provider = str(config.get("provider", "")).lower()
    provider_supported = provider in SUPPORTED_PROVIDERS

    return {
        "valid": not missing_fields and provider_supported,
        "missing_fields": missing_fields,
        "provider_supported": provider_supported,
        "provider": provider,
    }


def generate_storage_connection(config: Dict[str, Any]) -> Dict[str, Any]:
    """Generate mock storage connection metadata."""
    validation = validate_cloud_config(config)

    if not validation["valid"]:
        return {
            "connected": False,
            "reason": "Invalid cloud configuration",
            "validation": validation,
        }

    return {
        "connected": True,
        "provider": config["provider"],
        "service": config["service"],
        "region": config["region"],
        "resource": config.get("bucket")
        or config.get("container")
        or config.get("storage_account")
        or "default-storage-resource",
        "connection_mode": "mock",
    }


def generate_compute_spec(
    provider: str,
    workload_type: str,
    cpu: int = 4,
    memory_gb: int = 16,
    gpu_required: bool = False,
) -> Dict[str, Any]:
    """Generate a cloud compute specification for an ML workload."""
    provider = provider.lower()

    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    return {
        "provider": provider,
        "workload_type": workload_type,
        "cpu": cpu,
        "memory_gb": memory_gb,
        "gpu_required": gpu_required,
        "recommended_environment": (
            "gpu-enabled-training-node"
            if gpu_required
            else "standard-compute-node"
        ),
    }


def estimate_cloud_cost(
    cpu_hours: float,
    storage_gb: float,
    gpu_hours: float = 0,
) -> Dict[str, Any]:
    """Estimate simple cloud usage cost for demo purposes."""
    cpu_rate = 0.08
    storage_rate = 0.023
    gpu_rate = 1.25

    cpu_cost = cpu_hours * cpu_rate
    storage_cost = storage_gb * storage_rate
    gpu_cost = gpu_hours * gpu_rate

    total = cpu_cost + storage_cost + gpu_cost

    return {
        "cpu_cost": round(cpu_cost, 2),
        "storage_cost": round(storage_cost, 2),
        "gpu_cost": round(gpu_cost, 2),
        "estimated_total": round(total, 2),
        "currency": "USD",
        "note": "Demo estimate only; not tied to live provider pricing.",
    }


def create_model_artifact_location(
    provider: str,
    model_name: str,
    version: str,
    base_path: Optional[str] = None,
) -> Dict[str, str]:
    """Create a mock cloud path for storing model artifacts."""
    provider = provider.lower()

    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    base_path = base_path or f"{provider}://model-artifacts"

    return {
        "provider": provider,
        "model_name": model_name,
        "version": version,
        "artifact_uri": f"{base_path}/{model_name}/{version}/",
    }


def generate_deployment_environment(
    provider: str,
    environment_name: str,
    model_name: str,
    autoscaling: bool = True,
) -> Dict[str, Any]:
    """Generate a deployment environment plan."""
    provider = provider.lower()

    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    return {
        "provider": provider,
        "environment_name": environment_name,
        "model_name": model_name,
        "autoscaling": autoscaling,
        "status": "planned",
        "deployment_type": "real-time-endpoint",
    }


def check_cloud_readiness(config: Dict[str, Any]) -> Dict[str, Any]:
    """Check whether a cloud configuration is ready for agent workflow use."""
    validation = validate_cloud_config(config)

    checks = {
        "valid_config": validation["valid"],
        "has_storage_resource": any(
            key in config for key in ["bucket", "container", "storage_account"]
        ),
        "has_region": "region" in config,
        "has_service": "service" in config,
    }

    ready = all(checks.values())

    return {
        "cloud_ready": ready,
        "checks": checks,
        "recommendation": (
            "Cloud configuration is ready for workflow use."
            if ready
            else "Cloud configuration needs additional fields before use."
        ),
    }


def summarize_cloud_resources(configs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Summarize multiple cloud resource configs."""
    providers: Dict[str, int] = {}
    services: Dict[str, int] = {}

    for config in configs:
        provider = str(config.get("provider", "unknown")).lower()
        service = str(config.get("service", "unknown")).lower()

        providers[provider] = providers.get(provider, 0) + 1
        services[service] = services.get(service, 0) + 1

    return {
        "resource_count": len(configs),
        "providers": providers,
        "services": services,
    }
