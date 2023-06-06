

schema_1 = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "Title",
        "Season",
        "totalSeasons",
        "Episodes",
        "Response"
    ],
    "properties": {
        "Title": {
            "type": "string",
            "default": "",
            "title": "The Title Schema"
        },
        "Season": {
            "type": "string",
            "default": "",
            "title": "The Season Schema"
        },
        "totalSeasons": {
            "type": "string",
            "default": "",
            "title": "The totalSeasons Schema"
        },
        "Episodes": {
            "type": "array",
            "default": [],
            "title": "The Episodes Schema",
            "items": {
                "type": "object",
                "default": {},
                "title": "A Schema",
                "required": [
                    "Title",
                    "Released",
                    "Episode",
                    "imdbRating",
                    "imdbID"
                ],
                "properties": {
                    "Title": {
                        "type": "string",
                        "default": "",
                        "title": "The Title Schema"
                    },
                    "Released": {
                        "type": "string",
                        "default": "",
                        "title": "The Released Schema"
                    },
                    "Episode": {
                        "type": "string",
                        "default": "",
                        "title": "The Episode Schema"
                    },
                    "imdbRating": {
                        "type": "string",
                        "default": "",
                        "title": "The imdbRating Schema"
                    },
                    "imdbID": {
                        "type": "string",
                        "default": "",
                        "title": "The imdbID Schema"
                    }
                }
            }
        },
        "Response": {
            "type": "string",
            "default": "",
            "title": "The Response Schema"
        }
    }
}