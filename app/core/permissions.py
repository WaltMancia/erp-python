ROLE_PERMISSIONS = {

    "admin": [
        "products.view",
        "products.create",
        "products.edit",
        "products.delete",

        "inventory.view",

        "sales.view",

        "reports.view",

        "users.manage"
    ],

    "employee": [
        "products.view"
    ],

    "inventory": [
        "products.view",
        "inventory.view"
    ]
}


def has_permission(
    user,
    permission
):

    permissions = ROLE_PERMISSIONS.get(
        user.role,
        []
    )

    return permission in permissions
