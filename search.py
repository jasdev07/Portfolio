from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


# def search_users(args):
#     """Search users database

#     Parameters:
#         args: a dictionary containing the following search parameters:
#             id: string
#             name: string
#             age: string
#             occupation: string

#     Returns:
#         a list of users that match the search parameters
#     """

#     # Implement search here!
    
    
    

#     return USERS

def search_users(args):
    id_param = args.get("id")
    name_param = args.get("name")
    age_param = args.get("age")
    occupation_param = args.get("occupation")

    def user_priority_score(user):
        priority_score = 0

        if id_param is None or user["id"] == id_param:
            priority_score += 1000
        if name_param is None or name_param.lower() in user["name"].lower():
            priority_score += 100
        if age_param is None or (int(age_param) - 1 <= user["age"] <= int(age_param) + 1):
            priority_score += 10
        if occupation_param is None or occupation_param.lower() in user["occupation"].lower():
            priority_score += 1

        return priority_score

    sorted_users = sorted(USERS, key=user_priority_score, reverse=True)

    return [user for user in sorted_users if user_priority_score(user) > 0]



