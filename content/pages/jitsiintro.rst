Using Jitsi Meet
****************

:date: 2020-11-25
:summary: A tiny introduction
:save_as: index.html

.. container:: m-left-s m-col-m-3 m-container-inflate

    .. image:: {static}/images/jitsi-logo-deep-linking.png
        :target: https://jitsi.org/
        :alt: Jitsi logo

.. class:: m-noindent

	   
Jitsi Meet is an `open-source`_ video-conferencing application.  It looks a lot like other video-conferencing tools you may have used in the past, such as `Zoom`_, `Google Meet`_, or `Microsoft Teams`_.  Some things will look a bit different, and there will be slightly different-looking icons to click on, but the basic idea is the same.  Once you have used it a few times, you won't notice the difference.  Probably.

Why Jitsi?
----------

Zoom, Google Meet, and others do a good job.  They are reliable and easy to use, with world-spanning reach.  However, most of these applications are closed-source and run by for-profit companies.  A good and ancient rule of thumb for the Internet is that "when the product is free, *you* are the product."  In most cases, the way in which you become the product is through the harvesting of your personal information, which is then sold for profit.

Jitsi does not work in that way.  While it is free (as well as reliable and easy to use), your personal information is not harvested by the application, and there is nothing concealed in the code to do that.  The code itself is open source, free to look at and change.  Even better, you can set up Jitsi on your own server, which means that you are able to control the flow of information yourself.

For some organizations, anonymity of the participants in a meeting is important.  You do not need to set up an account to use Jitsi, and at least in my particular setup, your IP address is saved only for the length of the meeting and then discarded.

The particular incarnation of Jitsi discussed here is being run on one of my own private servers.  At the moment (March 1st, 2021) it lives on a virtual private server in New Jersey managed by `Linode`_.  But it will likely move around and the portability of the application is another attraction.  If you want (and know your way around Linux), you can set up a Jitsi server for your own use following the guide `here`_.

If you feel like checking out the public Jitsi Meet server, head on over to https://meet.jit.si

.. container:: m-row m-container-inflate

   .. container:: m-col-m-4

       .. block-info:: Participating in a meeting

           Joining a meeting is super-easy, and this will show you how

	   .. button-success:: {filename}/pages/joinmeeting.rst
               :class: m-fullwidth

               How to join a meeting

   .. container:: m-col-m-4	     

       .. block-warning:: Starting a meeting

           How to start a meeting (in this setup, only moderators can start / initialize a meeting)

	   .. button-warning:: {filename}/pages/jitsistartmeeting.rst
               :class: m-fullwidth

               How to start a meeting

   .. container:: m-col-m-4

       .. block-info:: Resources and links

           Links to download and install different Jitsi Meet applications - for Android, iOS, and desktop.  Also some places you can learn more about Jitsi!

	   .. button-info:: {filename}/pages/jitsilinks.rst
	       :class: m-fullwidth

	       Jitsi links








.. _open-source: https://en.wikipedia.org/wiki/Open_source
.. _Zoom: https://zoom.us/
.. _Google Meet: https://meet.google.com/
.. _Microsoft Teams: https://www.microsoft.com/en-us/microsoft-365/microsoft-teams/free
.. _Linode: https://www.linode.com/
.. _here: https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-start
.. _this page: {filename}/pages/christmas2020.rst

	  
