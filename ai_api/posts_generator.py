from gemini_api import get_completion

prompt = """
You are a professional productivity assistant and task organizer.

Based on the following settings, generate a well-structured task plan:

- Main Goal: {goal}
- Timeframe: {timeframe}
- Priority Level: {priority}
- Context: {context}

The output should include:
1. A clear breakdown of 5–7 actionable tasks toward the goal
2. Suggested deadlines or milestones within the given timeframe
3. Priority labeling for each task (High / Medium / Low)
4. Recommended tools, resources, or methods that could help
5. A short motivational note to encourage progress

Keep the plan concise, realistic, and easy to follow.
Reply only with the task plan, without extra explanations or formatting.
"""

goal = input("Enter the main goal: ")
timeframe = input("Enter the timeframe (e.g., 1 week, 1 month): ")
priority = input("Enter the priority level (High/Medium/Low): ")
context = input("Enter any context (e.g., work, study, personal): ")

prompt = prompt.format(goal=goal, timeframe=timeframe, priority=priority, context=context)

response = get_completion(prompt)
print(response)
