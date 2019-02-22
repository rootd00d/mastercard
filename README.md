# mastercard
Technical Interview Assignment for Mastercard

## DevOps Engineer Code Test

1. In any Linux based system (CentOS/RHEL preferred):

    a. Configure logrotate to rotate /var/log/httpd/access_log (or equivalent) hourly

    b. Configure an Apache HTTPD VirtualHost to do all of:

        i. Show a test page at https://example.com,

        ii. Redirect http to https, while maintaining all URL parameters,

        iii. Redirect www.example.com to example.com.

    c. Configure nginx as a load balancer to a local Apache HTTPD listening on 8080-8090

2. In your favourite programming language (PHP or Python preferred):

    a. Write code that will find a duplicate value in an array.

    b. Do the same for dictionaries.

3. We need to troubleshoot our website at https://www.mastercard.ca/. In any Linux based
system, use CLI tools to do the following (send us commands + outputs):

    a. Test if port 443 is answering at the IP address of our website.

    b. Check when the SSL certificate expires.

    c. Connect to http://www.mastercard.com/ using telnet and “GET /” (note: not https).

4. Package managers can be used to install software packages such as RPMs. Generally, companies and individuals host mirrors and package repositories in a website or ftp. An alternative is to use a system like AWS S3 to host a repository.    

    While public repositories are great, sometimes a privately hosted repository is desired for internal software. In these situations, you could host a private web server in your environment.

    Alternatively, a “serverless” approach could be to use S3 with an authentication scheme like IAM through the usage of a yum plugin. Write a value state / formula for a configuration management tool (SaltStack preferred) to install a S3 yum plugin (https://github.com/seporaitis/yum-s3-iam) and configure it.

5. Building an RPM for easy management of internal software is a common strategy to deploy
software. Create an RPM of a command line tool that prints out “Awe$ome”. Bonus: install this
in a fashion like #4 above.
Zip up all relevant files and send back to us.
Best regards, and good luck!