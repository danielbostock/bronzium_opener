# Bronzium Pack Opener

## Requirements

In order to use this application to open up your bronzium packs for you, you will need the following two things setup and basic knowledge on how to use them.

1. Star Wars Galaxy of Heroes (SWGOH) account in Google
2. BlueStacks setup and logged in with SWGOH account

## What does this application do?

In summary this application just repatively presses a keyboard key for you. This application will effectively keep pressing the '1' key repeatedly for as long as you define. BlueStacks has game controls which are like hot keys where you can use a key on your keyboard to provide an input to the BlueStacks game you are running.

## Why

If you are lazy like me, pressing the '1' as much as you would have to or clicking through the opening gets tedious and rather boring. There are other things whilst I have the time I would rather be doing. Thus I felt there should be a way to automate this whole process where I can go make dinner and packs can be opening for me while I do this or other things like going for a walk with my family as we so often do.

## Forewarning

It is imperative that you understand this application will continually press '1' on your keyboard, it actually has no respect or knowledge of BlueStacks, what this means is if you close BlueStacks, it will continue to run. You therefore cannot do anything else with your computer while this is running. It is intended to be used while you are away from keyboard (AFK) or if you were to run this in a Virtual Machine (VM). I will discuss this latter step in a more advanced topic and video seperately.

## TL;DR - Lets get started!

### GIF Guide

COMING SOON!


### Video Guide

COMING SOON!

### Text Guides

### Windows

##### Executable

**Step 1:** Download exe file here - <a href="https://1drv.ms/u/s!AqZNpR8_ZtGviKM-QTho_qw3sC3U-A?e=mfb9Qa">Bronzium Pack Opener v0.3a</a>

![install_download_exe](https://user-images.githubusercontent.com/53065247/119247797-0b2ca900-bbd0-11eb-8037-3a3a216cbbba.png)

**Step 2:** Unzip the file to a desired location

**Step 3:** Open BlueStacks and open SWGOH app

![install_open_bluestacks](https://user-images.githubusercontent.com/53065247/119247843-5b0b7000-bbd0-11eb-9151-05c11d9b8f1c.png)

**Step 4:** Navigate to the store and then select the bronzium pack. Your SWGOH screen should look like this
![store_bronzium_buy](https://user-images.githubusercontent.com/53065247/119247440-c2272580-bbcc-11eb-90c3-089979de43a7.png)

**Step 5:** Open the Bronzium Pack Opener that you downloaded and unzipped in step 2

![install_open_app](https://user-images.githubusercontent.com/53065247/119247872-9dcd4800-bbd0-11eb-92bb-329e5e2f4e78.png)

**Step 6:** Specify if you want this to run in a cyclic manner or a specified length of time. If you would like to know what each cycle means and what a length of time means for amount of packs opened or ally points spent, then refer to the chart below which gives you some rough number. Alternatively the default method will run it for 10 cycles or 35mins, which will consume 100k of ally points.

![app_specify](https://user-images.githubusercontent.com/53065247/119247901-cd7c5000-bbd0-11eb-8c2b-031887707e1d.png)

**Step 7:** Specify amount of cycles or length of time, again refer to chart to help inform your decision.

![app_specify_cycles](https://user-images.githubusercontent.com/53065247/119247977-53989680-bbd1-11eb-958e-bdba0fd03acb.png)

**Step 8:** After you have entered the amount of cycles or length of time, you will now need to confirm your run time for the application. You can either adjust your settings further or restart to go to change to a different run mode.

![image](https://user-images.githubusercontent.com/53065247/119247990-657a3980-bbd1-11eb-921d-b24550b486f1.png)

**Step 9:** Once you have started it, you will have 5 seconds to switch back to BlueStacks.

**Step 10:** The application should now start opening packs for you!


##### Source
**Step 1:** Clone or Download zip file of the repo from GitHub or directly links above

**Step 2:** If you downloaded as a zip file, unzip to desired if you downloaded as a zip file

**Step 3:** Open BlueStacks and open SWGOH app

**Step 4:** Navigate to the store and then select the bronzium pack. Your SWGOH screen should look like this

![store_bronzium_buy](https://user-images.githubusercontent.com/53065247/119247440-c2272580-bbcc-11eb-90c3-089979de43a7.png)

**Step 5:** Open launcher.py in the folder where you unzipped or cloned it to.

![install_open_py](https://user-images.githubusercontent.com/53065247/119247936-09afb080-bbd1-11eb-87e2-a8b31b8ae4c9.png)

**Step 6:** Specify if you want this to run in a cyclic manner or a specified length of time. If you would like to know what each cycle means and what a length of time means for amount of packs opened or ally points spent, then refer to the chart below which gives you some rough number. Alternatively the default method will run it for 10 cycles or 35mins, which will consume 100k of ally points.

![app_specify](https://user-images.githubusercontent.com/53065247/119247901-cd7c5000-bbd0-11eb-8c2b-031887707e1d.png)

**Step 7:** Specify amount of cycles or length of time, again refer to chart to help inform your decision.

![app_specify_cycles](https://user-images.githubusercontent.com/53065247/119247977-53989680-bbd1-11eb-958e-bdba0fd03acb.png)

**Step 8:** After you have entered the amount of cycles or length of time, you will now need to confirm your run time for the application. You can either adjust your settings further or restart to go to change to a different run mode.

![image](https://user-images.githubusercontent.com/53065247/119247990-657a3980-bbd1-11eb-921d-b24550b486f1.png)

**Step 9:** Once you have started it, you will have 5 seconds to switch back to BlueStacks.

**Step 10:** The application should now start opening packs for you!



### Mac

1.  After installing Docker Desktop, you should see a Docker icon in your menu bar. Click on it, and navigate to **Preferences** > **Kubernetes**.

2.  Check the checkbox labeled **Enable Kubernetes**, and click **Apply & Restart**. Docker Desktop will automatically set up Kubernetes for you. You'll know that Kubernetes has been successfully enabled when you see a green light beside 'Kubernetes _running_' in the Preferences menu.

3.  In order to confirm that Kubernetes is up and running, create a text file called `pod.yaml` with the following content:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: demo
    spec:
      containers:
      - name: testpod
        image: alpine:3.5
        command: ["ping", "8.8.8.8"]
    ```

    This describes a pod with a single container, isolating a simple ping to 8.8.8.8.

4.  In a terminal, navigate to where you created `pod.yaml` and create your pod:

    ```shell
    kubectl apply -f pod.yaml
    ```

5.  Check that your pod is up and running:

    ```shell
    kubectl get pods
    ```

    You should see something like:

    ```shell
    NAME      READY     STATUS    RESTARTS   AGE
    demo      1/1       Running   0          4s
    ```

6.  Check that you get the logs you'd expect for a ping process:

    ```shell
    kubectl logs demo
    ```

    You should see the output of a healthy ping process:

    ```shell
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: seq=0 ttl=37 time=21.393 ms
    64 bytes from 8.8.8.8: seq=1 ttl=37 time=15.320 ms
    64 bytes from 8.8.8.8: seq=2 ttl=37 time=11.111 ms
    ...
    ```

7.  Finally, tear down your test pod:

    ```shell
    kubectl delete -f pod.yaml
    ```

{% endcapture %}
{{ local-content | markdownify }}

</div>
<div id="kubewin" class="tab-pane fade" markdown="1">
{% capture localwin-content %}

### Windows

1.  After installing Docker Desktop, you should see a Docker icon in your system tray. Right-click on it, and navigate **Settings** > **Kubernetes**.

2.  Check the checkbox labeled **Enable Kubernetes**, and click **Apply & Restart**. Docker Desktop will automatically set up Kubernetes for you. You'll know that Kubernetes has been successfully enabled when you see a green light beside 'Kubernetes _running_' in the **Settings** menu.

3.  In order to confirm that Kubernetes is up and running, create a text file called `pod.yaml` with the following content:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: demo
    spec:
      containers:
      - name: testpod
        image: alpine:3.5
        command: ["ping", "8.8.8.8"]
    ```

    This describes a pod with a single container, isolating a simple ping to 8.8.8.8.

4.  In PowerShell, navigate to where you created `pod.yaml` and create your pod:

    ```shell
    kubectl apply -f pod.yaml
    ```

5.  Check that your pod is up and running:

    ```shell
    kubectl get pods
    ```

    You should see something like:

    ```shell
    NAME      READY     STATUS    RESTARTS   AGE
    demo      1/1       Running   0          4s
    ```

6.  Check that you get the logs you'd expect for a ping process:

    ```shell
    kubectl logs demo
    ```

    You should see the output of a healthy ping process:

    ```shell
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: seq=0 ttl=37 time=21.393 ms
    64 bytes from 8.8.8.8: seq=1 ttl=37 time=15.320 ms
    64 bytes from 8.8.8.8: seq=2 ttl=37 time=11.111 ms
    ...
    ```

7.  Finally, tear down your test pod:

    ```shell
    kubectl delete -f pod.yaml
    ```

{% endcapture %}
{{ localwin-content | markdownify }}
</div>
<hr>
</div>
