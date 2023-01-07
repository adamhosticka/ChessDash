"""Layout for player data visualization."""

import pandas as pd
from dash import Dash, html

from app.gui.player.players_count_per_country import PlayersCountPerCountry
from app.gui.player.players_rating_per_country import PlayersRatingPerCountry
from app.gui.player.status_rating_correlation import StatusRatingCorrelation
from app.gui.player.rating_correlation import \
    TacticsRatingCorrelation, PuzzleRatingCorrelation, JoinedRatingCorrelation, FollowersRatingCorrelation
from app.src.format_data.gui_format_players import convert_alpha2_code_to_alpha3


def player_layout(app: Dash, df: pd.DataFrame) -> html.Div:

    df['country'] = df['country_code'].apply(convert_alpha2_code_to_alpha3)
    df = df[df['player_id'].notna()]

    return html.Div(
        id='player_layout',
        children=[
            html.H1("Players dataset"),
            html.Br(),
            html.P(f"There are {df['player_id'].nunique()} unique players in the dataset from all around the world."),
            html.Hr(),
            html.Div(
                children=[
                    PlayersCountPerCountry(app, df).render(),
                    PlayersRatingPerCountry(app, df).render(),
                    StatusRatingCorrelation(app, df).render(),
                    TacticsRatingCorrelation(app, df).render(),
                    PuzzleRatingCorrelation(app, df).render(),
                    JoinedRatingCorrelation(app, df).render(),
                    FollowersRatingCorrelation(app, df).render(),
                ]
            )
        ]
    )
