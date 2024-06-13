from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):

    nome: Annotated[
        str,
        Field(
            description="Local de treinamento do atleta", examples="GYM", max_length=20
        ),
    ]

    endereco: Annotated[
        str,
        Field(
            description="Endereço do Local de treinamento",
            examples="Rua A, N° 123 - Cidade/Sigla Estado",
            max_length=60,
        ),
    ]

    prorietario: Annotated[
        str,
        Field(
            description="Dono do local de treinamento", examples="João", max_length=30
        ),
    ]


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="CT King",
            max_length=20,
        ),
    ]

    endereco: Annotated[
        str,
        Field(
            description="Endereço do centro de treinamento",
            example="Rua X, Q02",
            max_length=60,
        ),
    ]

    proprietario: Annotated[
        str,
        Field(
            description="Proprietario do centro de treinamento",
            example="Marcos",
            max_length=30,
        ),
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="CT King",
            max_length=20,
        ),
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]
