from functools import wraps
from sqlalchemy.orm import Session

class Transactional:
    def __call__(self, func):
        @wraps(func)
        async def _transactional(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                session : Session = kwargs.get('session')
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

            return result

        return _transactional
