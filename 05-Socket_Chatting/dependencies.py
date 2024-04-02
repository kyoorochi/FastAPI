# 인증 관련 추가 -> Token 기반으로 유저 네임값을 가져올 수 있도록 한다.

users = {
    1: {'username': 'test01'},
    2: {'username': 'test02'}
}

def get_username(token: str):
    # 토큰을 유저 ID로 간주
    user_id = int(token)
    user = users.get(user_id)

    return user['username']