from authentication.enum.roles import Role
from common.guards.factory_guard import create_role_permission

IsAdmin = create_role_permission(Role.ADMIN.value)
IsWorker = create_role_permission(Role.WORKER.value)
IsUser = create_role_permission(Role.USER.value)