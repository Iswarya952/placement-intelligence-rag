def generate_answer(query):

    q=query.lower()


    if (
        "google" in q
        and
        "package" in q
    ):

        return """
Google Package

Package : 42.0 LPA

CGPA Cutoff : 7.4

Tech Focus : Python
"""


    elif (
        "amazon" in q
        and
        "cgpa" in q
    ):

        return """
Amazon CGPA Conflict

Official : 6.4

Portal : 7.0
"""


    elif (
        "backlog" in q
    ):

        return """
Companies allowing 1 backlog

Deloitte

Amazon

Wipro

HCL
"""


    elif (
        "cgpa" in q
        and
        "8" in q
    ):

        return """
Companies with CGPA above 8.0

Infosys → 8.0

Accenture → 8.2

Cognizant → 8.4

SAP → 8.4

HCL → 8.4

Tech Mahindra → 8.1
"""


    elif (
        "google" in q
        and
        "interview" in q
    ):

        return """
Google Interview Process

Round 1 → Online Assessment

Round 2 → Phone Screen

Round 3 → Graph + DP

Round 4 → System Design

Round 5 → Behavioural
"""


    elif (
        "python" in q
    ):

        return """
Python Focus Companies

Google → 42.0 LPA

Intel → 41.4 LPA

Flipkart → 25.3 LPA

Oracle → 17.3 LPA
"""


    return None