# Add the following to let students access courses without configuration
# For more information, read Notes for Instructors in the documentation
c.CourseDirectory.course_id = '*'

from nbgrader.auth import JupyterHubAuthPlugin
c = get_config()
c.Exchange.timezone = 'Hongkong'
c.Exchange.path_includes_course = True
# c.Authenticator.plugin_class = JupyterHubAuthPlugin

c.Exchange.root = '/tmp/exchange'
c.TransferApp.path_includes_course = True