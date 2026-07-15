# 10. Monitoring

## Purpose

Monitoring is the continuous observation of an AI agent or workflow
after deployment. Unlike traditional software, AI agents can change
behavior over time due to model updates, knowledge changes, prompt
revisions, tool failures, or shifting user requests.

This chapter explains how to monitor AI agents regardless of whether
they are implemented using n8n, LangGraph, CrewAI, OpenAI Agents SDK,
AutoGen, or another framework.

------------------------------------------------------------------------

# Learning Objectives

After reading this chapter, you should be able to:

-   Explain why monitoring is essential.
-   Identify the key categories of monitoring.
-   Define meaningful operational metrics.
-   Distinguish monitoring from evaluation.
-   Design dashboards and alerts.
-   Monitor multi-agent systems.
-   Track cost, latency, and quality over time.

------------------------------------------------------------------------

# Why Monitoring Matters

Monitoring answers the question:

> **"Is my AI system still working correctly today?"**

Without monitoring, problems often go unnoticed:

-   Hallucinations increase.
-   APIs fail silently.
-   Costs rise unexpectedly.
-   Latency grows.
-   Routing errors appear.
-   Human review queues become overloaded.

------------------------------------------------------------------------

# What Should Be Monitored

## 1. Performance

Typical metrics:

  Metric              Description
  ------------------- ---------------------------------------
  Response time       End-to-end completion time
  Tool latency        Time spent waiting for external tools
  Workflow duration   Total execution time
  Throughput          Requests handled per minute

Example:

``` text
User
  │
  ▼
Router (30 ms)
  │
Retriever (220 ms)
  │
LLM (1.8 s)
  │
Response
```

------------------------------------------------------------------------

## 2. Quality

Quality metrics include:

-   Task completion rate
-   Hallucination rate
-   Citation accuracy
-   Customer satisfaction
-   Grounded responses

Example targets:

  Metric                  Target
  ----------------------- --------
  Hallucinations          \<1%
  Citation accuracy       \>99%
  Successful completion   \>95%

------------------------------------------------------------------------

## 3. Cost

Monitor:

-   Token usage
-   API spend
-   Embedding cost
-   Search cost

Example:

  Component      Daily Cost
  ------------ ------------
  LLM                  \$24
  Embeddings            \$5
  Search                \$7
  Total                \$36

------------------------------------------------------------------------

## 4. Reliability

Track:

-   Failures
-   Retries
-   Timeouts
-   Invalid outputs
-   Tool availability

------------------------------------------------------------------------

## 5. Tool Monitoring

Each tool should have independent metrics.

  Tool       Success Rate
  -------- --------------
  Search            99.3%
  CRM               99.8%
  Email             99.9%

------------------------------------------------------------------------

## 6. Routing Monitoring

For multi-agent systems monitor:

-   Delegation accuracy
-   Routing loops
-   Escalation frequency
-   Dead ends

------------------------------------------------------------------------

## 7. Memory Monitoring

Track:

-   Retrieval accuracy
-   Duplicate memories
-   Stale memories
-   Memory growth

------------------------------------------------------------------------

## 8. Security Monitoring

Watch for:

-   Prompt injection
-   Unauthorized tool use
-   Suspicious request patterns
-   Data leakage attempts

------------------------------------------------------------------------

# Logging vs Monitoring

Logging records events.

``` text
10:15 Search Tool Success
```

Monitoring analyzes trends.

``` text
Search failures increased by 35%.
Alert generated.
```

Logs answer **what happened**.

Monitoring answers **is the system healthy**.

------------------------------------------------------------------------

# Observability

Three pillars:

1.  Logs
2.  Metrics
3.  Traces

Example trace:

``` text
User
 ↓
Router
 ↓
Research Agent
 ↓
Search
 ↓
Summarizer
 ↓
Response
```

------------------------------------------------------------------------

# Dashboards

A useful dashboard typically includes:

-   Request volume
-   Average latency
-   Cost
-   Success rate
-   Human reviews
-   Tool failures

------------------------------------------------------------------------

# Alerts

Suggested alert thresholds:

  Alert                    Trigger
  ------------------------ -------------
  High latency             \>5 s
  Cost spike               \>20% daily
  Tool failure             \>10%
  Hallucination increase   \>2%

------------------------------------------------------------------------

# Human Review Monitoring

Track:

-   Approval rate
-   Override rate
-   Review backlog
-   Average review time

------------------------------------------------------------------------

# Multi-Agent Monitoring

Additional metrics:

-   Delegation count
-   Coordination latency
-   Workflow completion
-   Conflict resolution rate

------------------------------------------------------------------------

# Best Practices

-   Monitor quality as well as speed.
-   Measure cost continuously.
-   Alert only on meaningful thresholds.
-   Monitor every external tool separately.
-   Review dashboards regularly.
-   Keep detailed audit logs.
-   Use traces for debugging complex workflows.

------------------------------------------------------------------------

# Common Mistakes

-   Monitoring only latency.
-   Ignoring hallucinations.
-   Not tracking cost.
-   Never reviewing logs.
-   Alerting on every small issue.
-   Ignoring human corrections.

------------------------------------------------------------------------

# Relationship to Other Chapters

  -----------------------------------------------------------------------
  Chapter                       Relationship
  ----------------------------- -----------------------------------------
  09 Evaluation                 Evaluation validates before deployment.
                                Monitoring validates after deployment.

  08 Human Review               Monitoring measures review workload and
                                overrides.

  11 Security                   Monitoring detects security incidents.

  12 Multi-Agent Systems        Adds coordination metrics and routing
                                visibility.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Summary

Monitoring provides continuous visibility into an AI system after
deployment. Effective monitoring combines performance, quality,
reliability, cost, security, routing, memory, and human review metrics
to ensure agents remain trustworthy, efficient, and safe over time.

