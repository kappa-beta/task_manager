class TaskService:
    def __init__(self, session=Depends(get_session), settings=Depends(get_settings)):
        self.session = session
        self.settings = settings

    def create_task(self, account_create: AccountCreate):
        task = Task(
            email=account_create.email,
            username=account_create.username,
        )
        self.session.add(account)
        try:
            self.session.commit()
            return account
        except IntegrityError:
            raise EntityConflictError from None
