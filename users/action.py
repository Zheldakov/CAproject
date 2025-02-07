from users.models import Action


def journal_user_action(user, action):
    action = Action(user=user, action=action)
    action.save()