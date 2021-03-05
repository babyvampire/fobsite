Joining a Jitsi meeting
***********************

:date: 2020-12-22
:summary: How to join a Jitsi meeting

.. role:: text-small
    :class: m-text m-small

Simply couldn't be easier.  Generally someone will send you a link to the meeting by text or email, and you can simply click on it.  If you are on a computer, the link will open in your default browser (though Google Chrome will usually work better, if it is not your default browser).  If you are on a smartphone or tablet, you will (usually, depending on your settings), be directed to a page that will allow you to use the app (if it is already installed) or download the app (if it is not already installed).	    

`I'm on a computer`_
=======================

.. class:: m-text m-noindent

The easiest and simplest way to join a meeting, for most people, will be to use your web browser.  At this time, the browser which works the best for Jitsi is Google Chrome.  Other browsers will work but could occasionally cause problems.

Another nice, clean way to use Jitsi on your computer is to use their open source Electron application.  This allows you to bypass any of the problems that can arise with different browsers' varying implementation of the technologies underlying Jitsi, such as WebRTC.  Instructions on how to install the dedicated computer application can be found on the Jitsi Meet Electron `Github page`_

`I'm using a smartphone or some other small device!`_
=====================================================

.. class:: m-text m-noindent

If you are using a smartphone of some type, the most reliable (and recommended) way to use Jitsi is by installing the relevant app for your device and joining a meeting through that app. And, if you are using a Windows or MacOS computer, you can install a desktop application that will work reliably.  Links to smartphone and desktop applications can be found in the `Useful Links section`_ of this website.

`OK, I've got the link, now what?`_
===================================

.. class:: m-text m-noindent

You will have been given a link to the meeting, which might look something like this: ``https://meet.fob.monster/MeetingName``.  The **MeetingName** part of the address is the part that might change from meeting to meeting.  For this server, the first part of the address will *always* be **meet.fob.monster**.  And for our meetings at Pine Grove, the link will almost always be ``https://meet.fob.monster/pinegrove``.

.. class:: m-text m-noindent

Paste or type this link into the address bar of your browser, and press <RETURN> (Fig 1).  In most browsers you will be able to dispense with the "``https://``" part and can simply type ``meet.fob.monster/pinegrove``



.. figure:: {static}/images/enteringJitsiMeetURLinChrome.png
     :alt: entering the URL into chrome address bar

     :text-small:`Fig 1: Enter the meeting URL into the address bar (Google Chrome)`

.. container:: m-row

    .. container:: m-col-t-6

       .. figure:: {static}/images/waitingForHost.png
			 :alt: Waiting for the host

			 :text-small:`Fig 2: Waiting for the host`

    .. container:: m-col-t-6

      .. class:: m-text

		 If the meeting has not yet started, you will see this message (Fig 2).  And if you aren't the host, you'll just have to wait!  If you *are* the host, then follow the instructions in the `Starting a Meeting`_ section.

		 [if this message remains after the meeting *should* have started, then check to make sure you have the correct meeting name/link, and/or message the person running the meeting]

`Grant permission to use camera and microphone`_
================================================

The first time you use Jitsi Meet (and probably most of the time, depending on your browser's security settings), it will ask for your permission to use your camera and microphone.  Grant this permission by clicking on :label-info:`Allow`.

.. container:: m-row m-container-inflate

    .. container:: m-col-s-4

        .. figure:: {static}/images/allowJitsiCameraMicrophoneChrome.jpg
            :figclass: m-flat
            :alt: Chrome asking permission

            ..

            .. class:: m-text m-small m-noindent

            Chrome asking permission

    .. container:: m-col-s-4

        .. figure:: {static}/images/allowJitsiCameraMicrophoneFirefox.jpg
            :figclass: m-flat
            :alt: Firefox asking permission

            ..

            .. class:: m-text m-small m-noindent
            
            Firefox asking permission

    .. container:: m-col-s-4


        .. figure:: {static}/images/allowJitsiCameraMicrophoneSafari.jpg
            :figclass: m-flat
            :alt: Safari asking permission

            ..

            .. class:: m-text m-small m-noindent
            
            Safari asking permission
		 
`At the meeting`_
=================

If you have played your cards right, you will now be looking at a screen much like this one (**Fig 3**).  Below Figure 3 is an explanation of the different parts of the screen - but hopefully some of them will make sense at first sight.

At first entry into the meeting, the screen will have its focus on you.  On the right side of the screen, in this view, are the other participants in the meeting.  If you wish to see any of the other participants in full view, click on their images - they will then occupy the largest part of the screen.
		 
.. figure:: {static}/images/jitsiConsole.jpg
    :target: {static}/images/jitsiConsole.jpg
    :alt: the Jitsi Console

    :text-small:`Fig 3: The Jitsi Console`

       
.. class:: m-table

+--+--------------+------------------------------------------------------+  
|# | Component    | Function                                             |
+==+==============+======================================================+
|1 | Chat         | Text chat with everyone in the meeting               |
+--+--------------+------------------------------------------------------+
|2 | Screen Share | Share your screen with others in the meeting         |
+--+--------------+------------------------------------------------------+
|3 | Raise Hand   | Raise or lower your hand                             |
+--+--------------+------------------------------------------------------+
|4 | Mute / Unmute| Enable or disable your microphone                    |
+--+--------------+------------------------------------------------------+
|5 | Leave        | Hang up and leave the meeting                        |
+--+--------------+------------------------------------------------------+
|6 | Camera       | Enable or disable your video                         |
+--+--------------+------------------------------------------------------+
|7 | Tile view    | Toggle the tile view of all participants             |
+--+--------------+------------------------------------------------------+
|8 | Invite       | Share the meeting link so others may join            |
+--+--------------+------------------------------------------------------+
|9 | Security     | Security options                                     |
+--+--------------+------------------------------------------------------+
|10| More options | Further options include managing your video quality, |
|  |              | sharing a YouTube video, and your personal settings. | 
|  |              | (Some of the options are not currently enabled)      |
+--+--------------+------------------------------------------------------+

.. _Useful Links section: {filename}/pages/jitsilinks.rst	   
.. _Starting a Meeting: {filename}/pages/jitsistartmeeting.rst
.. _Github page: https://github.com/jitsi/jitsi-meet-electron
