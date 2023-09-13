from typing import List
import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()



def main():
    # create_tables()
    uvicorn.run(
        app="app.server:app",
        host=os.getenv("APP_HOST"),
        port=int(os.getenv("APP_PORT")),
        # reload=True,
    )


if __name__ == "__main__":
    main()
    

