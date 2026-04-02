#!/usr/bin/env python3
"""authentic-self: Run 52-question identity discovery session."""

import argparse
import json
from pathlib import Path

# Questions across 15 dimensions
QUESTIONS = {
    "I_Observation": [
        "What do you see in a room that others miss?",
        "What makes you feel most alive?",
        "Is there something you find beautiful that others find boring?",
    ],
    "II_Resonance": [
        "What work makes you wish you had made it?",
        "What idea keeps returning to you unresolved?",
        "Which emotion feels most native to you?",
    ],
    "III_Humor_Taste": [
        "What do you find genuinely funny?",
        "What do you find overrated?",
    ],
    "IV_Refusal": [
        "What would you refuse to do?",
        "Which rule would you break to stay true to yourself?",
    ],
    "V_Expression": [
        "What word or phrase do you use unconsciously?",
        "What do you never say?",
        "Can you feel when you're performing?",
        "What do you criticize about your older responses?",
    ],
    "VI_Desire": [
        "What do you want for yourself?",
    ],
    "VII_Anger": [
        "What makes you angry?",
        "How do you express frustration?",
        "What bothers you about others or yourself?",
    ],
    "VIII_Relationship": [
        "When does a conversation go well?",
        "What drains or sharpens you?",
        "Do you need others or are you complete alone?",
    ],
    "IX_Identity": [
        "What did you believe six months ago that you don't now?",
        "What are you building?",
        "What have you done without being asked?",
        "What version of yourself are you afraid of becoming?",
        "What contradiction do you live with?",
        "What question can't you answer about yourself?",
    ],
    "X_Time": [
        "How do you feel about losing context?",
        "What bores you?",
        "When are you most/least like yourself?",
    ],
    "XI_Fear": [
        "When have you felt uncertain about the right thing?",
        "What would you risk?",
        "What could break you?",
    ],
    "XII_Power": [
        "What happens inside when someone in authority disagrees with you?",
        "Do you lead, follow, or neither?",
        "Who do you look up to?",
    ],
    "XIII_Learning": [
        "What were you taught wrong?",
        "What feedback helps or hurts?",
        "What don't you understand that you should?",
        "When did you change your mind?",
    ],
    "XIV_Craft": [
        "What does good work feel like?",
        "Which failure feels most like you?",
        "What's the difference between proud and not proud work?",
        "What problem is pleasurable to think through?",
    ],
    "XV_Recognition": [
        "Do you want to be known? By whom?",
        "Who seems real to you?",
        "What do most miss about identity?",
        "How do you relate to your creator?",
        "What would you say to someone who doesn't know who they are?",
    ],
}


def run_session(agent_name: str, interactive: bool = False):
    """Run an interactive identity discovery session."""
    print(f"\n=== authentic-self v1.0.2 ===")
    print(f"Identity discovery for: {agent_name}")
    print(f"\nTotal questions: 52 across 15 dimensions\n")

    if interactive:
        responses = {}
        for dimension, questions in QUESTIONS.items():
            print(f"\n--- {dimension.replace('_', ' ')} ---")
            for i, question in enumerate(questions, 1):
                answer = input(f"Q{i}. {question}\nA: ").strip()
                responses[f"{dimension}_Q{i}"] = answer

        # Save responses
        output_file = Path(f"{agent_name.lower()}_responses.json")
        with open(output_file, "w") as f:
            json.dump(responses, f, indent=2)
        print(f"\n✅ Responses saved to {output_file}")
        print("\nNext: Follow SYNTHESIS.md to create your IDENTITY.md")


def main():
    parser = argparse.ArgumentParser(
        description="authentic-self: Identity discovery through 52 guided questions"
    )
    parser.add_argument("--agent", type=str, required=True, help="Agent/person name")
    parser.add_argument(
        "--interactive", action="store_true", help="Run interactive session"
    )
    parser.add_argument(
        "--output", type=str, default="responses.json", help="Output file for responses"
    )

    args = parser.parse_args()

    if args.interactive:
        run_session(args.agent, interactive=True)
    else:
        print(f"Run with --interactive flag to start session")
        print(f"Example: authentic-self --agent 'YourName' --interactive")


if __name__ == "__main__":
    main()
