
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from fastapi.responses import HTMLResponse
app = FastAPI(
    title="WWE Players Info API",
    description="A mini project to manage WWE player profiles and match records.",
    version="1.0.0"
)


@app.get("/welcome", response_class=HTMLResponse)
def welcome_page():
    return """
    <html>
        <head>
            <title>WWE Players Info</title>
        </head>
        <body style="background:#111827;color:white;
                     font-family:Arial;text-align:center;padding:80px">
            <h1>🔥 WWE PLAYERS INFO</h1>
            <h2>Welcome to the WWE Universe!</h2>
            <p>Built with Python + FastAPI </p>
            <a href="/docs" style="color:#60a5fa">
                (Learn Build Share) Explore API Documentation
            </a>
        </body>
    </html>
    """

# Demo data for our project
players = {
    1: {
        "id": 1,
        "name": "John Cena",
        "nickname": "The Champ",
        "brand": "Free Agent",
        "championships": 16,
        "wins": 250,
        "losses": 40,
        "matches": [
            {
                "opponent": "Randy Orton",
                "result": "Win",
                "event": "WrestleMania"
            },
            {
                "opponent": "Roman Reigns",
                "result": "Loss",
                "event": "SummerSlam"
            }
        ]
    },
    2: {
        "id": 2,
        "name": "Roman Reigns",
        "nickname": "The Tribal Chief",
        "brand": "SmackDown",
        "championships": 6,
        "wins": 180,
        "losses": 25,
        "matches": [
            {
                "opponent": "Cody Rhodes",
                "result": "Loss",
                "event": "WrestleMania"
            }
        ]
    },
    3: {
        "id": 3,
        "name": "Cody Rhodes",
        "nickname": "The American Nightmare",
        "brand": "Raw",
        "championships": 3,
        "wins": 120,
        "losses": 30,
        "matches": []
    }
}


# Request models
class MatchRecord(BaseModel):
    opponent: str
    result: str
    event: str


class PlayerCreate(BaseModel):
    name: str
    nickname: str
    brand: str
    championships: int = Field(default=0, ge=0)
    wins: int = Field(default=0, ge=0)
    losses: int = Field(default=0, ge=0)


class PlayerUpdate(BaseModel):
    nickname: str | None = None
    brand: str | None = None
    championships: int | None = Field(default=None, ge=0)
    wins: int | None = Field(default=None, ge=0)
    losses: int | None = Field(default=None, ge=0)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to WWE Players Info API!",
        "docs": "/docs",
        "welcome_page": "/welcome",
        "total_players": len(players)
    }


# Get all players
@app.get("/players")
def get_players():
    """
    Get a list of all WWE players.
    """
    return list(players.values())


# Search players by name
@app.get("/players/search")
def search_players(name: str):
    results = [
        player for player in players.values()
        if name.lower() in player["name"].lower()
    ]

    if not results:
        raise HTTPException(
            status_code=404,
            detail="No players found with that name"
        )

    return results


# Get a player's complete profile and match history
@app.get("/players/{player_id}")
def get_player(player_id: int):
    if player_id not in players:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    return players[player_id]


# Add a new player
@app.post("/players", status_code=201)
def add_player(player: PlayerCreate):
    """Add a new WWE player to the system."""
    new_id = max(players.keys(), default=0) + 1

    new_player = {
        "id": new_id,
        **player.model_dump(),
        "matches": []
    }
    players[new_id] = new_player
    return {
        "message": "Player added successfully!",
        "player": new_player
    }


# Update player details
@app.put("/players/{player_id}")
def update_player(player_id: int, update: PlayerUpdate):
    if player_id not in players:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    changes = update.model_dump(exclude_unset=True)

    players[player_id].update(changes)

    return {
        "message": "Player updated successfully!",
        "player": players[player_id]
    }


# Add a match record
@app.post("/players/{player_id}/matches", status_code=201)
def add_match(player_id: int, match: MatchRecord):
    if player_id not in players:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    if match.result.lower() not in {"win", "loss", "draw", "no contest"}:
        raise HTTPException(
            status_code=400,
            detail="Result must be Win, Loss, Draw, or No Contest"
        )

    match_data = match.model_dump()
    match_data["result"] = match_data["result"].title()

    players[player_id]["matches"].append(match_data)

    return {
        "message": "Match record added successfully!",
        "player": players[player_id]["name"],
        "match": match_data
    }


# Get match history
@app.get("/players/{player_id}/matches")
def get_match_history(player_id: int):
    if player_id not in players:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    return players[player_id]["matches"]


# Delete a player
@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    if player_id not in players:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    deleted_player = players.pop(player_id)

    return {
        "message": "Player deleted successfully!",
        "player": deleted_player["name"]
    }
