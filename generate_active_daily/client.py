from typing import AsyncIterator, Dict, List
from urllib.parse import urljoin

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from .constants import LEETCODE_BASE_URL


async def query_question_of_today():
    transport = AIOHTTPTransport(url=f"{LEETCODE_BASE_URL}/graphql/")

    async with Client(
        transport=transport, fetch_schema_from_transport=False
    ) as session:
        query = gql(
            """
            query questionOfToday {
                activeDailyCodingChallengeQuestion {
                    date
                    # userStatus
                    link
                    question {
                    #   acRate
                    difficulty
                    #   freqBar
                    frontendQuestionId: questionFrontendId
                    #   isFavor
                    paidOnly: isPaidOnly
                    #   status
                    title
                    titleSlug
                    #   hasVideoSolution
                    #   hasSolution
                    codeDefinition
                    content
                    # topicTags {
                    #   name
                    #   id
                    #   slug
                    # }
                    }
                }
            }
            """
        )

        result = await session.execute(query)
        return result


async def query_previous_question(current_question_slug, env_id, env_type):
    transport = AIOHTTPTransport(url="https://leetcode.com/graphql/")
    async with Client(
        transport=transport,
        fetch_schema_from_transport=False,
    ) as session:
        query = gql(
            """
            query learningContext($currentQuestionSlug: String!, $categorySlug: String, $envId: String, $envType: String, $filters: QuestionListFilterInput) {
                learningContextV2(
                currentQuestionSlug: $currentQuestionSlug
                categorySlug: $categorySlug
                envId: $envId
                envType: $envType
                filters: $filters
                ) {
                    name
                    backLink
                    previousQuestion {
                        difficulty
                        title
                        titleSlug
                        questionFrontendId
                        paidOnly
                    }
                }
            }
            """
        )
        params = {
            "currentQuestionSlug": current_question_slug,
            "envId": env_id,
            "envType": env_type,
        }
        result = await session.execute(query, variable_values=params)
        return result["learningContextV2"]["previousQuestion"]


async def query_qd_challenge_question(title_slug):
    transport = AIOHTTPTransport(url="https://leetcode.com/graphql/")
    async with Client(
        transport=transport,
        fetch_schema_from_transport=False,
    ) as session:
        # query = gql("""
        #   query qdChallengeQuestion($titleSlug: String!) {
        #     question(titleSlug: $titleSlug) {
        #       titleSlug
        #       title
        #       questionFrontendId
        #       challengeQuestion {
        #         date
        #         type
        #       }
        #     }
        #   }
        #   """
        # )
        query = gql(
            """
            query qdChallengeQuestion($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    challengeQuestion {
                        date
                    }
                }
            }
            """
        )
        params = {"titleSlug": title_slug}
        return (await session.execute(query, variable_values=params))["question"][
            "challengeQuestion"
        ]


async def previous_questions(limit: int) -> AsyncIterator[List[Dict[str, str]]]:
    if limit <= 0:
        return

    todays_question = (await query_question_of_today())[
        "activeDailyCodingChallengeQuestion"
    ]

    todays_slug = todays_question["question"]["titleSlug"]
    todays_env_id = todays_question["date"]
    # AFAICT this will never change for our purposes
    todays_env_type = "daily-question"
    previous_question = await query_previous_question(
        todays_slug, todays_env_id, todays_env_type
    )
    yield previous_question
    count = 1
    while count < limit:
        prev_slug = previous_question["titleSlug"]
        previous_question = await query_previous_question(
            prev_slug, todays_env_id, todays_env_type
        )
        if not previous_question["paidOnly"] is False:
            # Continue the loop again, until paidOnly is False
            continue
        count += 1
        yield previous_question


def make_leetcode_url_from_slug(title_slug):
    """Generates a URL to the well-known /problems/ path for a question slug"""
    base_url = urljoin(LEETCODE_BASE_URL, "/problems/")
    return urljoin(base_url, title_slug + "/")
