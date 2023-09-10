from fastapi import APIRouter, Query, Path, Header, HTTPException, status
from starlette.responses import JSONResponse
import requests


from creating_models import UserCreateRequest
from response_models import UserInfoResponse


# create app
router = APIRouter(prefix="/api-users")


@router.post("/")
async def create_user(item: UserCreateRequest):
    input = item.model_dump()
    output = UserInfoResponse(input)
    return output


@router.get("/{item_id}")
async def read_user_info(item_id: int, response_model=UserInfoResponse):
    url = f"http://api.example.com/users/{item_id}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        user_info = {
            "id": data["id"],
            "status": data["status"],
            "name": data["name"],
            "team_id": data["team_id"],
            "team_name": data["team_name"],
            "social_networks": data["social_networks"],
            "img": data["img"],
            "description": data["description"],
            "stack": data["stack"],
            "interests": data["interests"],
        }
        return user_info

    return None


@router.get("/{item_id}/stats")
async def user_stats(item_id: int = Path(..., example="999")):
    return {"id": item_id}


@router.post("/query")
async def query_user(name: str = Query(..., example="Masha")):
    return name


@router.post("/headers")
async def user(x_api_key: str = Header(..., example="2.718271")):
    if x_api_key != "3.1415":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )

    return "ok"


# team endpoints


# hacks endpoints


# catalog endpoints
