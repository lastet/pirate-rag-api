import os
import requests

API_URL = "http://127.0.0.1:8000/query"


def run_semantic_test(test_name: str, question: str, must_contain: list[str]) -> None:
    """
    Semantic test for RAG retrieval quality.

    Expectation: in Mock LLM mode the API returns retrieved context directly,
    so we validate presence of anchor keywords from docs.
    """
    url = f"{API_URL}?q={question}"
    response = requests.post(url)

    if response.status_code != 200:
        raise Exception(
            f"☠️ [{test_name}] SERVER ERROR\n"
            f"Status: {response.status_code}\n"
            f"URL: {url}\n"
            f"Body: {response.text}\n"
        )

    answer = response.json().get("answer", "")
    answer_lc = answer.lower()

    missing = [kw for kw in must_contain if kw.lower() not in answer_lc]

    if missing:
        raise AssertionError(
            f"❌ [{test_name}] FAILED (retrieval mismatch)\n"
            f"Question: {question}\n"
            f"Expected keywords: {must_contain}\n"
            f"Missing keywords: {missing}\n"
            f"Got answer/context:\n{answer}\n"
        )

    print(
        f"✅ [{test_name}] PASSED\n"
        f"Question: {question}\n"
        f"Found keywords: {must_contain}\n"
    )


def test_pancakes():
    run_semantic_test(
        test_name="pirate_pancakes",
        question="How do I make pancakes?",
        must_contain=["salt de mer", "eggs", "rum"],
    )


def test_apple_pie():
    run_semantic_test(
        test_name="pirate_apple_pie",
        question="What ingredients are used for apple pie?",
        must_contain=["apples", "cinnamon", "rum"],
    )


def test_mashed_potatoes():
    run_semantic_test(
        test_name="pirate_mashed_potatoes",
        question="How to make mashed potatoes?",
        must_contain=["potatoes", "salt de mer", "liquor"],
    )


def test_omelette():
    run_semantic_test(
        test_name="pirate_omelette",
        question="How to make an omelette?",
        must_contain=["eggs", "salt de mer", "morning whiskey"],
    )


if __name__ == "__main__":
    print(f"🧪 USE_MOCK_LLM={os.getenv('USE_MOCK_LLM', '(not set)')}\n")

    test_pancakes()
    test_apple_pie()
    test_mashed_potatoes()
    test_omelette()

    print("🏴‍☠️ All semantic tests passed — the galley is seaworthy.")
