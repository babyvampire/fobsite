Some useful Jitsi links
***********************

:date: 2020-12-04
:summary: Links for various Jitsi things

This page will discuss the various non-browser applications available for hosting and participating in Jitsi meetings.

.. contents::
   :class: m-block m-default

`Smartphone apps`_
==================

You can use a browser (preferably, at the moment, Google Chome) to join and start meetings if you are on a smartphone or tablet.  However, most device manufactures embed proprietary or limited versions of audio, video, and communication frameworks which limit the ability of smartphone web browsers to use Jitsi effectively.

This means that on devices such as iPhones or Android phones and tablets, using a dedicated app designed by the Jitsi community will give you (and other participants!) the best results.

[I don't particularly enjoy installing apps on my phone - applications produced by most organizations manage to squeeze in all kinds of tracking and privacy-violating functions.  In this case, however, the apps are open-source and the privacy components are verifiable.  If you have an Android device, my suggestion will always be to install the F-Droid version.  F-Droid is a trustworthy source for free and open source software for the Android platform - they pay careful attention to privacy and closed-source concerns and evaluate each package before they offer it. You will have to download the F-Droid app first, before you install software from them.]

Here are links to the Jitsi app at the Apple app store (for iOS devices such as iPhones and iPads), the Google Play Store (for Anfroid devices), and F-Droid (a good repository for open-source Android apps):

.. container:: m-row m-container-inflate

   .. container:: m-col-t-4

      .. image:: {static}/images/app-store-badge.png
	 :target: https://apps.apple.com/us/app/jitsi-meet/id1165103905/
	 :alt: Apple app store

   .. container:: m-col-t-4

      .. image:: {static}/images/google-play-badge.png
	 :target: https://play.google.com/store/apps/details?id=org.jitsi.meet&hl=en&gl=US
		  
   .. container:: m-col-t-4
		  
      .. image:: {static}/images/f-droid-badge.png
	 :target: https://f-droid.org/en/packages/org.jitsi.meet/

`Configuring your smartphone app`_
==================================

If you are planning on using a particular Jitsi server regularly, your app will work better if you designate the Jitsi server in the app's settings.

Below is a screen recording I made of adding the ``meet.fob.monster`` server to the Android app's preferences.  This will look and work in a similar manner for all apps.

.. raw:: html

   <style>

	 video {
	        width: 30vw;
	}
	
   </style>
   
.. raw:: html
	 
   <center>
     <video id="jitsiVideo" controls
     poster="{static}/media/jitsiInstallScreenRecordingCover.png"> 
        <source src="{static}/media/jitsiAppScreenRecordingSmaller.mp4" type="video/mp4">
     Your browser does not support the video tag.
     </video>
   </center>

.. raw:: html

   <script>

   var vid = document.getElementById("jitsiVideo");

   vid.playbackRate = 1.5;
 
   </script> 	 


`Dedicated desktop / laptop application`_
=========================================

For Windows, MacOS, and Linux machines, there are dedicated Electron-based applications that are easy to install and will avoid some of the peculiarities of the various web browsers currently available.  If you plan on using Jitsi much, it will be worthwhile to install this app on your device.

You will need to configure the application to use a particular Jitsi server - in our case you would want to set it to ``meet.fob.monster`` but you could configure it to use ``meet.jit.si`` or any other server to which you have access.

Here is the link to the Github page with download links and instructions:

`Github page for the Jitsi Meet Electron application`_



.. _Github page for the Jitsi Meet Electron application: https://github.com/jitsi/jitsi-meet-electron


		  
