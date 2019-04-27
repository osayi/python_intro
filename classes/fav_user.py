import users_class
import admin_class

fav_user = admin_class.Admin('ivy','agbons')
fav_user.describe_user()

new_admin = admin_class.Admin('sayi','ao')
new_admin.describe_user()
new_admin.priv.show_privileges()
 
