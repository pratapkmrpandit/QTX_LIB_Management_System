from models import sessionlocal,Task

def create_task(title,description):
    session=sessionlocal()
    new_task=Task(title=title,description=description)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    session.close()
    return new_task

def get_tasks():
    session=sessionlocal()
    task=session.query(Task).all()
    session.close()
    return task

def update_task(task_id,status):
    session=sessionlocal()
    task=session.query(Task).filter(Task.id==task_id).first()
    if task:
        task.status=status
        session.commit()

    session.close()
    return task

def delete_task(task_id):
    session=sessionlocal()
    task=session.query(Task).filter(Task.id==task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()
    return task

if __name__ == "__main__":
    # Create tasks
    create_task("Learn SQLAlchemy", "Understand ORM basics")
    create_task("Build Project", "Use SQLAlchemy for CRUD")

    # View tasks
    for t in get_tasks():
        print(t.id, t.title, t.status)

    # Update a task
    update_task(1, "Completed")

    # Delete a task
    delete_task(2)

    # View tasks after update/delete
    for t in get_tasks():
        print(t.id, t.title, t.status)