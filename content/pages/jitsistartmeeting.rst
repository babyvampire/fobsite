Starting a Jitsi Meeting
************************

:date: 2020-12-1
:summary: Starting a Jitsi Meeting

Excellent, we have a meeting to start!

This page will walk you through the process of starting and hosting a meeting.

.. note-dim::
   :class: m-text m-dim

	   Although this is all discussed in the context of hosting a meeting with a bunch of people, Jitsi can work just as well as a one-to-one video chat.  If you want to have a video chat with one person, you can go through the process below but pick your own unique meeting name, then send that URL to the person with whom you wish to speak.

.. contents::
   :class: m-block m-default
	  
`Go to our Jitsi Meet home page`_
=================================

Go to the URL of our Jitsi-Meet server: https://meet.fob.monster (preferably using Google Chrome\ [1]_ or a smartphone app). This is the important part of the page that you will see:

.. figure:: {static}/images/jitsiLandingPage.jpg
    :scale: 50%
    :figclass: m-flat
    :alt: Pine Grove Jitsi landing page

    ..

    .. class:: m-text m-small m-noindent

    The prompt to start a meeting

`Choose the name of the meeting`_
=================================

In the "Start meeting" text box, enter the name of the meeting you would like to start.  This name is important, since the way other people will join the meeting will be by going to the URL::

   https://meet.fob.monster/[name of meeting]


`(Use a pre-designated meeting name, if there is one)`_
=======================================================

If this is a meeting that we have publicized in advance, then you should start the meeting with that name.  For example, if the name of our weekly meeting is ``pinegrove``, then enter that name into the text box and click :label-info:`GO` (or press [return]).  The link that other people will use to join our meeting will then be ``https://meet.fob.monster/pinegrove``.


`Grant permission to use camera and microphone`_
================================================

The first time you use Jitsi Meet (and probably most of the time, depending on your browser's security settings), it will ask for your permission to use your camera and microphone.  Grant this permission by clicking on :label-info:`Allow`.

.. container:: m-row m-container-inflate

    .. container:: m-col-m-4

        .. figure:: {static}/images/allowJitsiCameraMicrophoneChrome.jpg
            :figclass: m-flat
            :alt: Chrome asking permission

            ..

            .. class:: m-text m-small m-noindent

            Chrome asking permission

    .. container:: m-col-m-4

        .. figure:: {static}/images/allowJitsiCameraMicrophoneFirefox.jpg
            :figclass: m-flat
            :alt: Firefox asking permission

            ..

            .. class:: m-text m-small m-noindent
            
            Firefox asking permission

    .. container:: m-col-m-4


        .. figure:: {static}/images/allowJitsiCameraMicrophoneSafari.jpg
            :figclass: m-flat
            :alt: Safari asking permission

            ..

            .. class:: m-text m-small m-noindent
            
            Safari asking permission


`Confirm you are an authorized host`_
=====================================

.. container:: m-row

    .. container:: m-col-m-7 m-left-m

	.. class:: m-text
		   
	    * Authorized hosts are the only people who can start a meeting on this particular server, and they will have been given usernames and passwords through some sneaky sidechannel.  More likely, we will just have a generic username and password that can authorize anyone as a host.  When you click the :label-info:`GO` button to start a meeting, a window will pop up telling you that the meeting has not yet started.  Click on the :label-info:`I am the host` button.

    .. container:: m-col-s-6 m-center-s m-col-m-5 m-right-m 
            
        .. figure:: {static}/images/JitsiHostPrompt.png
            :figclass: m-flat
            :alt: Jitsi asking if you are the host

            ..

            .. class:: m-text m-small m-noindent

            Jitsi asking if you are the host

.. container:: m-row

    .. container:: m-col-m-7 m-left-m 

        .. class:: m-text
            
            * After you click on :label-info:`I am the host`, a window will pop up asking for your username and password.  It will suggest the format "user@domain.net" for the username, but we are using simple one word usernames.  Enter the username and password that you have been given, press [return] or click :label-info:`OK`.
	      
	      Note that once you have started a meeting, anyone can join it - and they can do so anonymously.  The only part that is protected right now is *starting* a meeting.  There is a mechanism for making a meeting password protected, which we could talk about instituting at a later time if we feel it is necessary.

    .. container:: m-col-s-6 m-center-s m-col-m-5 m-right-m
    
        .. figure:: {static}/images/passwordRequired.png
            :figclass: m-flat
            :alt: the username and password box

            ..

            .. class:: m-text m-small m-noindent

            Username and password request box for host

.. note-dim::

   Leaving a Jitsi-Meet server completely open would allow anyone who stumbled upon it to start hosting meetings.  The only reason this might be an issue is due to the confusion that would result from this happening, especially for first-time users of the platform.  We ran into this problem with Zoom, where people trying to attend a meeting would inadvertently start hosting it.  To avoid this possible issue, a username and password are currently required to host a meeting on the ``fob.monster`` server.  The username and password will be distributed through another means, probably a friendly text message.

Things we can add later, if we want
===================================

There are a whole bunch of other things that we could set up, if we think they might be useful.

.. container:: m-row

    .. container:: m-col-m-7 m-left-m

	.. class:: m-text
		   
		   * **Passwords** We can set a password for the meeting, which could be distributed beforehand.  This is a pretty common thing for video conferencing, and something that Zoom instituted early on to prevent hooligans from joining and disrupting meetings.

		     There are a couple of drawbacks to this from our perspective - one is that the meeting link and the password would probably be distributed in the same way (i.e., semi-publicly) and so having a password would be redundant.  Another is that it does kind of go against the basic philosophy of our fellowship - it would be like locking the door to a meeting.  Anyway, it's always an option!

		     Passwords can be set after creating a meeting (see image).

    .. container:: m-col-s-6 m-center-s m-col-m-5 m-right-m

        .. figure:: {static}/images/jitsiSettingPassword.gif
            :figclass: m-flat
            :alt: setting a meeting password

            ..

            .. class:: m-text m-small m-noindent

            Setting a meeting password

.. container:: m-row

    .. container:: m-col-m-7 m-left-m

	.. class:: m-text
		   
		   * **Pre-join page** We could enable what is called a "pre-join" page, which appears before someone joins a meeting.  This allows them to choose a name, mute themselves, and see if their microphone is working. This might be useful if someone hasn't used the platform before.

    .. container:: m-col-s-6 m-center-s m-col-m-5 m-right-m

        .. figure:: {static}/images/jitsiPreMeetingScreen.png
            :figclass: m-flat
            :alt: pre-join screen

            ..

            .. class:: m-text m-small m-noindent

            what the pre-join screen would look like

.. container:: m-row

    .. container:: m-col-m-7 m-left-m

	.. class:: m-text
		   
		   * **Lobby** If we ever want to have more control over who enters the meeting, we could institute a *lobby* for the meeting.

		     When a lobby is set up for a meeting, anyone following the link for the meeting first ends up on a preliminary page in which they enter their name and request permission to join (see top image).
		     On the screen of the authorized host, a notice pops up showing who is requesting permission to join - the host may accept or reject the participant (see bottom image).

		     I would have some of the same concerns here as with setting a password, but it could be a useful option in some other context.

    .. container:: m-col-s-6 m-center-s m-col-m-5 m-right-m

	.. figure:: {static}/images/jitsiLobbyAskingToJoinMeeting.png
	    :figclass: m-flat
	    :alt: A participant waiting in the lobby

	    ..

	    .. class:: m-text m-small m-noindent

	    Potential participant waiting in the lobby

	.. figure:: {static}/images/jitsiKnockingFromLobby.png
	    :figclass: m-flat
	    :alt: Host sees someone knocking from the lobby

	    ..

	    .. class:: m-text m-small m-noindent

	    Look, someone cool is asking to join our meeting!
	    

.. [1] At the moment, the Google Chrome browser works a little better than Firefox or Safari due to some limitations in the way that Firefox implements WebRTC.  If the meeting only has a few people in it (up to 10) this might not matter too much.  This is likely to be fixed in later versions of Firefox (? about Safari) - but for now Google Chrome is the suggested browser to use. See `this section`_ for a discussion of how to use Jitsi using a smartphone app (Android or iOS) or a desktop application.


.. _this section: {filename}/pages/jitsilinks.rst



