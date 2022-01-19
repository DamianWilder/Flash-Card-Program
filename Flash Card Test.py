# Program to simulate flash cards for studying for test material for NOS110, Operating Systems Concepts

import random

# look at importing OS to get_terminal_size for outputting strings to proper width
FLASH_CARDS = {
    # Chapter 1 terms
    "1": {
        "accelerometer": "A device that detects the physical tilt and acceleration of the device.",
        "application (app)": "Software that allows a computer user to perform useful functions such as writing a report or calculating a budget. Commonly called an “___.”",
        "central processing unit (CPU)": "An integrated circuit (chip) that performs the calculations, or processing, for a computer. Also called a microprocessor.",
        "client": "A software component that accesses services of a network server.",
        "command-line interface (CLI)": "A user interface that consists of a character-based command line that provides only sparse amounts of information.",
        "computer": "A device that performs calculations.",
        "Chrome OS": "An operating system based on a Linux kernel with a GUI based on the Chrome web browser.",
        "cursor": "In a command-line interface (CLI), the cursor is merely a marker for the current position where what you type on the keyboard will appear. In a GUI, a graphical pointer that can have a variety of shapes you can move around by manipulating a pointing device sometimes replaces the cursor.",
        "device driver": "Software that is added to an OS to control a physical component (device). Each unique hardware device connected to a computer needs a component-specific device driver.",
        "device management": "An OS function that controls hardware devices using device drivers.",
        "directory": "A special file that can contain files as well as other directories. This term is most often used with non-GUI operating systems. When describing a directory in a GUI, the commonly used term is folder.",
        "distribution": "A bundling of the Linux kernel and software—both enhancements to the OS and applications. Applications may include word processors, spreadsheets, media players, and more.",
        "embedded OS": "An operating system stored in firmware, as in a mobile device.",
        "file management": "An operating system function that allows the operating system to read, write, and modify data and programs organized into files.",
        "file system": "The logical structure used on a storage device for storing files, as well as the code within an operating system that allows the OS to store and manage files on a storage device.",
        "firmware": "Software resident in integrated circuits.",
        "folder": "A term describing a type of file that can contain other folders as well as files—most often used with GUI operating systems. When describing a ____ in a non-GUI operating system, people most often use the term directory.",
        "formatting": "The process that writes the logical structure of a file system on a storage device.",
        "graphical user interface (GUI)": "A user interface that takes advantage of a computer’s graphics capabilities to make it easier to use with graphical elements that one can manipulate to perform tasks, such as system and file management and the running of applications.",
        "input/output (I/O)": "Anything sent into a computer (input); anything coming out of a computer (output). Every keystroke you enter, all files read in, and even voice commands are input. Output can include a printed page, what you see on the screen, and even sounds.",
        "integrated circuit (IC)": "A small electronic component made up of transistors (tiny switches) and other miniaturized parts.",
        "Internet of Things (IoT)": "Devices not normally associated with computer that contain microcomputers and are connected to networks. These devices include, but are not limited to: kitchen appliances, thermostats, utility meters, components in automobiles, light bulbs, and industrial control devices.",
        "job management": "An operating system function that controls the order and time in which programs are run. For example, an operating system's print program can manage and prioritize multiple print jobs.",
        "kernel": "The main component of an operating system, which always remains in memory while a computer is running.",
        "killer app": "An application that many people need enough to purchase a computer that will run that app.",
        "Mac": "The product name for Apple’s computers.",
        "memory": "The physical chips that store programs and data. There are two basic types: random-access memory (RAM) and read-only memory (ROM).",
        "memory management": "An operating system function that manages and tracks the placement of programs and data in memory. Advanced operating systems, such as Windows, Linux, and macOS use memory management to make optimal use of memory.",
        "microcomputer": "A computer built around a microprocessor.",
        "microprocessor": "An integrated circuit (chip) that performs the calculations, or processing, for a computer. Also called a processor or central processing unit (CPU).",
        "mobile device": "A hand-help device that uses wireless technologies.",
        "motherboard": "The central circuit board of a computer to which all other devices connect.",
        "multitasking": "Two or more programs (tasks) running simultaneously on a computer.",
        "New Technology File System (NTFS)": "An expandable file system used by the Windows OS. It uses transaction processing to track changes to files and includes many other features. The most important of these features are file and folder security and file encryption.",
        "operating system (OS)": "A collection of programs that provides a computer with critical functionality, such as the user interface, management of hardware and software, and ways of creating, managing, and using files.",
        "partition": "An area of a storage device where the logical structure of a single file system may reside.",
        "personal computer (PC)": "A computer running Windows or Linux.",
        "portable operating system": "An operating system that you can use on a variety of computer system platforms, with only minor alterations required to be compatible with the underlying architecture.",
        "processes": "Components of a program that are active in memory.",
        "random-access memory (RAM)": "Memory that acts as the main memory for holding active programs.",
        "screen rotation": "A feature of mobile operating systems that takes advantage of the built-in hardware accelerometer in a device by rotating the image on the screen to accommodate the device’s position and allow you to read the screen.",
        "security": "An operating system function that provides password-protected authentication of the user before allowing access to the local computer. Security features may restrict what a user can do on a computer.",
        "server": "A computer that plays one or more of several important roles in a network. In all these roles, it provides services to other computers (clients).",
        "smartphone": "A device that works as a cell phone but also lets you connect to the Internet, view your email, and install a variety of apps for entertainment, education, and work.",
        "solid-state drive (SSD)": "A storage device that uses integrated circuits, which can be written to and read from much faster than conventional hard disk drives and optical drives.",
        "system firmware": "Program code that informs the processor of the devices present and how to communicate with them.",
        "system on a chip (SoC)": "The single microchip containing all or most of the electronic circuity required for a device.",
        "tablet": "A mobile device that has a touch screen, no integrated keyboard (usually), is larger than a smartphone, and is much more portable than a laptop computer.",
        "task management": "An operating system function in multitasking OSs that controls the focus. The user can switch between tasks by bringing an application to the foreground, which gives the focus to that application.",
        "user interface (UI)": "The software layer, sometimes called the shell, through which the user communicates with the OS, which, in turn, communicates with the computer hardware.",
        "virtual keyboard": "A screen image of a keyboard with labeled keys that you can tap to enter characters when required.",
    },
    # Chapter 3 terms
    "3": {
        "application virtualization": "A type of virtualization in which a user connects to a server and accesses one or more applications rather than an entire desktop environment.",
        "augmented reality (AR)": "viewing something in real time through a camera or other device while the image (or other input) is digitally modified.",
        "avatar": "An animated computer-generated human used in a virtual world to represent an individual.",
        "desktop virtualization": "The software virtualization of a desktop computer into which you can install an operating system.",
        "dumb terminal": "A device consisting of little more than a keyboard and display with a connection to a host computer (mainframe or minicomputer) and having no native processing power of its own (hence the term dumb).",
        "guest OS": "An operating system running within a virtual machine.",
        "host key": "A key combination used to release control of the keyboard and mouse from within a virtual machine so that they can be used in the host OS.",
        "host OS": "The operating system installed directly on a computer and into which a virtual machine is installed.",
        "hypervisor": "The software layer that emulates the necessary hardware on which an operating system runs, allowing multiple operating systems to run simultaneously on a single computer.",
        "ISO file": "an image of the contents of a CD or DVD.",
        "network virtualization": "a network addressing space that exists within one or more physical networks, but which is logically independent of the physical network structure.",
        "Second-Level Address Translation (SLAT)": "A feature found in many newer Intel and AMD CPUs and required by some hypervisors.",
        "server virtualization": "Virtualization in which a single machine hosts multiple virtual servers, each of which performs tasks as independently from the others as separate physical machines would.",
        "storage virtualization": "Virtualization of networked data storage in which client computers can utilize many networked hard drives as though they are one.",
        "terminal client": "Client software that enables a user to connect to server-based terminal services that provide an environment, called a partition, in which the user accesses programs on the server.",
        "terminal services": "A server-based service that creates individual environments, called partitions, within which a user can work in programs after remotely connecting over a network.",
        "thin client": "A low-cost PC, usually without such common peripherals as diskette drives (now gone from most PCs), expansion slots, and optical drives. The purpose of a thin client is to connect to a server, allowing the user to work in a server-hosted environment.",
        "Type I hypervisor": "A hypervisor that can run directly on a computer without an underlying host operating system.",
        "Type II hypervisor": "A hypervisor that requires a host operating system.",
        "Type II hypervisor": "A hypervisor that requires a host operating system.",
        "virtual machine (VM)": "A virtual environment that emulates a computer and supports the installation of an operating system.",
        "virtual reality (VR)": "A virtual environment that includes three-dimensional images and involves other senses, giving the participant a feeling of actually being present in that time and space.",
        "virtual world": "A computer-based environment inhabited by animated computer-generated human stand-ins (called avatars). An individual uses an avatar to represent themselves within the virtual world, interacting with other avatars.",
        "virtualization": "The creation of an environment that seems real but isn’t.",
        "Windows XP Mode": "Windows Virtual PC with a free and legal Windows XP VM preinstalled. Only available in certain editions of Windows 7.",
    },
    # Chapter 5 terms
    "5": {
        "bloatware": " Slang for the software added to a computer when it is purchased with Windows preinstalled. Some of these programs are useful, but most of it is annoying or may be free trial software that you can try, but must purchase to use after the trial period expires.",
        "continuum": "A feature for working on a two-in-one device. With the keyboard attached, Windows 10 displays in PC-style Desktop mode. Detach the keyboard and the ____ feature automatically changes to Tablet mode on the fly.",
        "Cortana": "____ is an intelligent search system that searches the Web, your computer or device, and any cloud storage you use from that computer. You do not need to remember a syntax with Cortana, instead you can ask questions as if you are talking with a person. Cortana also learns about you, not by spying but by paying attention to things you give her permission to watch, using the Notebook feature.",
        "desktop mode": "Windows 10 ____ ____ displays the Start menu covering a portion, but not all, of the Desktop.",
        "device manager": "A Control Panel applet that displays the list of hardware and the status of each device.",
        "domain joined": "A feature that allows a Windows computer to join a Microsoft Active Directory Domain.",
        "Ease of Access": "A Windows feature for configuring audio and visual aids for those who need them.",
        "FIDO Alliance": "An industry consortium in which the members, representing industries such as banking, software, hardware, and more can contribute their technology and work together to develop solutions to allow users to securely access online services and conduct financial transactions without using password authentication to reduce the risk of fraud. FIDO is an acronym for Fast Identity Online.",
        "File Explorer": "The Windows file management tool in Windows 8.1 and Windows 10, previously named Windows Explorer.",
        "Hey Cortana": "A voice activation option that was introduced in Windows Phone 8.1 and made available to Windows 10 for those devices that support voice input. It takes some training of the app by the user to ensure that Cortana responds to the voice query.",
        "keyboard shortcut": "A key combination that performs an assigned action, saving you several mouse or keyboard actions.",
        "live tile": "A rectangular object on the Windows 8.1 Start screen and the Windows 10 Start menu that, when tapped with a finger or clicked with a mouse, launches an app. The “live” part of the name is due to a tile’s ability to display active content related to the app without requiring you to launch the app.",
        "lock screen": "A screen that displays after Windows 8.1 start up. It also displays when Windows is locked or when a period of inactivity triggers the screen saver. You must use a swiping motion to close the Lock screen and access either the Sign-in screen or the Start screen.",
        "Microsoft Account (MSA)": "A free account with Microsoft that gives the subscriber access to Microsoft services, such as Outlook.com, Messenger, OneDrive, and Xbox Live.",
        "Microsoft Edge": "An alternative to the decades-old Internet Explorer (IE), which is also included in Windows 10 for backward compatibility with some websites.",
        "Microsoft Passport": "____ ____ lets you securely sign in to network resources without sending a password or PIN over the network; the authentication is tied to the hardware.",
        "multitouch": "The ability to interpret multiple simultaneous touch gestures, such as the pinching gesture in which fingers first touch the device (screen, touch mouse, or touch pad) at separate locations and then pinch together while in contact with the device.",
        "Out of Box Experience (OOBE)": "A feature on a new computer with Windows 8.1 or Windows 10 preinstalled. When you take it out of the box and turn it on, you will be greeted with this last phase of Windows installation where you personalize the GUI and configure how you will sign in. Of course, it is also the last phase of a clean Windows installation.",
        "picture-in-picture (PIP)": "The Xbox app supports ____-____-____ ____ in which one show displays on the screen while another displays in a small box. This has been a feature of TVs for decades.",
        "predictive notification": "Providing a notice or other information in anticipation of a need.",
        "quick link": "What was called a shortcut on the Start menu in Windows 7 is now called a ____ ____.",
        "start button": "A graphical button on the far left of the task bar that opens the Start menu.",
        "tablet mode": "A mode in which all apps run full screen that is activated when Windows 10 wakes up on a tablet without an attached keyboard. The Start menu opens full screen (Tablet mode) to work better with a touch screen. Manually switch to Tablet mode using the Tablet mode button in the Action Center.[Action Center contains all notifications in one place, as well as convenient buttons to change settings.]",
        "task view": "Windows 10 ____ ____ lets you quickly view all your open apps and improves on the Windows 7 Aero Flip 3D feature. In addition, use ____ ____ to switch between Virtual Desktops.",
        "two-step verification": "A way to provide a second step beyond just using password authentication. It adds extra security. When you configure your Microsoft account with ____-____ ____, you provide a telephone number where you can receive text messages. When Microsoft uses ____-____ ____, it shows the last two digits of your phone number and you respond with the last four digits. Then the system texts you a numeric code on your phone which you then enter as a verification code.",
        "universal app": "A ____ ____ (type of app) conforms to different screen sizes and other features, such as input type (keyboard/mouse vs. touch screen) and makes the switch automatically.",
        "user tile": "A tile at the very top of the left pane of the Start menu for the currently signed-in user, with a picture, if the user chooses to add one.",
        "Virtual Desktop": "A ____ ____ allows you to group your projects into multiple desktops. For instance, on a home PC you could create a personal finance Desktop with windows for Quicken, Excel, a calculator app, and your personal banking website open in one ____ ____. [The generic term for Virtual Desktops is “workspaces.”]",
        "Web-based setup": "An online Windows setup, available through the Microsoft website for upgrading to Windows 10.",
        "Web Note": "A tool that lets you mark up and save a Web page by allowing you to write or draw on the page, highlight items, erase your annotations, clip a portion of a page, and save the Web page with your annotations. You can then share it with other people.",
        "Windows 10 Home Edition": "____ ____ ____ ____ runs on PCs and tablets and is aimed at consumers who do not need some of the premium features of Windows 10 Pro.",
        "Windows 10 Pro": "____ ____ ____ runs on PCs and tablets. It is equivalent to the Windows 8.x Pro, Windows 7 Professional, and Windows 7 Ultimate operating systems that offer features required for business.",
        "Windows Hello": "A new biometric sign-in feature that lets you sign in to your Windows 10 device with a biometric sign-in such as fingerprint, facial recognition, or iris scan. It requires the existence of special hardware in the Windows 10 computer.",
        "Windows key": "A key located near the bottom left of most keyboards with a Windows logo on it. It is used alone and in combination with other keys as keyboard shortcuts.",
        "Windows Setup": "The traditional program for installing and upgrading Windows. It is run from disc or from the source files.",
        "Xbox Game bar": "If you have an Xbox One, Windows 10 lets you access your Xbox data such as friends, activity, game history, and record video game clips. The Xbox Game bar contains buttons that let you record games, take screenshots of games, and configure Xbox.",
    },
    # Chapter 6 terms
    "6": {
        "binary file": "A file that contains program code, as opposed to a file containing data.",
        "bootloader": "The Windows OS startup code that gets loaded in memory.",
        "bootstrap loader": "A firmware program that uses hardware configuration settings stored in nonvolatile memory (commonly called CMOS) to determine what devices can start an OS and the order in which the system will search these devices while attempting to begin the OS startup process.",
        "code signing": "A practice introduced in Windows 2000 in which all of the operating system code is digitally signed to show that it has not been tampered with.",
        "Command Prompt": "A command-line interface (CLI) that you can launch from within Windows, from Safe Mode, or as a Recovery option.",
        "Consent Prompt": "A prompt requesting permission from an administrator to proceed with an action that requires administrator privileges.",
        "Credentials Prompt": "A prompt requesting that a standard user provide computer administrator credentials before granting permission to proceed with an action that requires administrator privileges.",
        "data type": "A special data format in the Windows registry. There are several registry data types, such as REG_BINARY, REG_DWORD, and so forth.",
        "Device Stage": "A Windows 7 feature which, if the device supports it, will bring up a page from which you can make many choices for managing the device, and it often includes an accurate image of the device.",
        "digital signature": "In Windows, encrypted data that can be unencrypted by Windows in a process called file signature verification.",
        "driver signing": "Code signing of device drivers that indicates two things: the integrity of the file or files, and that the device driver has passed Microsoft’s tests for compatibility.",
        "Early Launch Anti-Malware (ELAM)": "A security component that examines each of the device drivers before they load into memory, thus preventing suspicious drivers from loading.",
        "Fast Boot": "A start-up feature that takes advantage of the hibernated kernel of the Windows 8 Hybrid Shutdown by bring the hibernated system session out of hibernation, saving all the work of the Kernel Loading phase.",
        "file signature verification": "The process by which Windows unencrypts a digital signature and verifies that the file has not been tampered with in any way.",
        "Hibernate": "The process of saving to disk an image of the contents of RAM, including the OS, open apps, and all the associated data before the OS sends the command to power down the computer.",
        "hive": "The portion of the Windows registry represented in one registry file.",
        "Hybrid Shutdown": "In Windows 8, when you select Shutdown from the Power menu it 1) sends messages to all running apps to save data and settings and then it shuts down the apps, 2) closes the session for each logged-on user, and 3) hibernates the Windows session and saves it in a file.",
        "key": "In the Windows registry, a folder object that may contain one or more sets of settings as well as other keys.",
        "Last Known Good Configuration": "A startup option that starts Windows normally and selects the configuration that existed at the last successful user logon, ignoring changes made after the last logon.",
        "logon phase": "The phase of startup that includes authenticating the user, starting the Windows Logon service, runs existing logon scripts during program startup, and starts plug-and-play detection.	",
        "Measured Boot": "A UEFI firmware feature that logs the start-up process so antimalware software can analyze this log to determine if malware is on the computer or if the boot components were tampered with.",
        "MSCONFIG": "The System Configuration Utility, a Windows tool for modifying system start-up, allows you to modify and test start-up configuration settings without having to alter the settings directly. It allows you access to settings buried within the registry and allows you to make the changes temporary or permanent.",
        "plug and play": "The ability of a computer to automatically detect and configure a hardware device. To work, the computer, the device, and the OS must all comply with the same ____ ____ ____ standard.",
        "power-on self-test (POST)": "A series of firmware program tests of the system hardware that determines the amount of memory present and verifies that devices required for OS startup are working.",
        "registry": "A database of all configuration settings in Windows.",
        "root key": "In the Windows registry, the top five folders are ____ ___s, often called subtrees in Microsoft documentation. Each of these subtrees is the top of a hierarchical structure containing folders called keys.",
        "Safe Mode": "A mode for starting Windows with certain drivers and components disabled.",
        "Safe Mode with Command Prompt": "A mode for starting Windows with only a command prompt as a user interface.",
        "Secure Boot": "The UEFI firmware feature that loads only trusted operating system bootloaders.",
        "security ID (SID)": "A unique string of numbers preceded by S-1-5 that identifies a security principal in a Windows security accounts database.",
        "Sleep": "The ____ power option causes the computer to stay on in a very-low-power mode; the system state and user session (applications and data) are saved in RAM, but the screen turns off.",
        "subkey": "In the Windows registry, a key that exists within another key.",
        "System Recovery Command Prompt": "An advanced command-line interface where you can enter commands to repair Windows.",
        "Trusted Boot": "A Windows 8 feature that examines each of the system files required for the boot process before it loads into memory.",
        "Unified Extensible firmware Interface (UEFI)": "A standard for system firmware in modern computers that replaced the decades old ROM-BIO.",
        "value entry": "A setting within a Windows registry key.",
        "warm boot": "A restart of the firmware and operating system without a power down and power up cycle.",
        "Windows PowerShell": "A command-line interface (CLI) that accepts text input and accepts objects, as defined by object-oriented programming.",
        "Windows Recovery Environment (Windows RE)": "A component of Windows PE that, when needed, provides support with a powerful group of diagnostic and repair tools. ",
    },
}

MENU_CHOICES = ("MODE", "HELP", "DONE", "START", "CHAPTERS")
CHAPTERS_LIST = ("1", "3", "5", "6")


def main():
    show_welcome()
    show_menu()
    program_running = True
    mode = "remembered"
    chapters = []
    while program_running:
        selection = get_user_choice()
        if selection == "MODE":
            mode = select_mode(mode)
        elif selection == "CHAPTERS":
            chapters = get_chapters()
        elif selection == "HELP":
            show_menu()
        elif selection == "START":
            print()
            if not chapters:
                print("You must select at least one chapter before beginning")
            else:
                begin_studying(mode, chapters)
        elif selection == "DONE":
            print()
            program_running = False


def begin_studying(mode, chapters):
    print()
    answer_key = [key for i in chapters for key in FLASH_CARDS[i]]
    if mode == "standard":
        random.shuffle(answer_key)
        correct_counter = 0
        for key in answer_key:
            correct_answer = key
            for i in FLASH_CARDS:
                if FLASH_CARDS[i].get(key):
                    print(FLASH_CARDS[i][key])
                    print()
                else:
                    continue
            answer = input("Answer: ")
            if answer.upper() == correct_answer.upper():
                print("Correct!")
                correct_counter += 1
                print()
            elif answer == "done":
                quit_early = input("Would you like to exit early (y/n)? ")
                if quit_early == "y":
                    print()
                    break
            else:
                print(f"Correct answer:{key}")
                print()
        print(
            f"You got {correct_counter} answers correct out of {len(answer_key)}. That's {correct_counter / len(answer_key)}%!"
        )

    elif mode == "remembered":
        testing = True
        random.shuffle(answer_key)
        already_correct = []
        while testing:
            correct_counter = 0
            for key in answer_key:
                correct_answer = key
                for i in FLASH_CARDS:
                    if FLASH_CARDS[i].get(key):
                        print(FLASH_CARDS[i][key])
                        print()
                    else:
                        continue
                answer = input("Answer: ")
                if answer.upper() == correct_answer.upper():
                    print("Correct!")
                    correct_counter += 1
                    already_correct.append(correct_answer)
                    print()
                elif answer == "done":
                    quit_early = input("Would you like to exit early (y/n)? ")
                    if quit_early == "y":
                        print()
                        break
                else:
                    print(f"Correct answer: {key}")
                    print()
            print(
                f"You got {correct_counter} answers correct out of {len(answer_key)}. That's {round((correct_counter / len(answer_key)) * 100, 2)}%!"
            )
            print()
            play_again = input("Play again (y/n)? ")
            print()
            if play_again == "y":
                for i in answer_key[::]:
                    if i in already_correct:
                        answer_key.remove(i)
                if not answer_key:
                    print("You already got everything right! Exiting to main menu")
                    print()
                    testing = False
                    break
            else:
                print("Exiting to main menu")
                print()
                testing = False
                break


def show_welcome():
    print(
        """
    Welcome to the NOS 110 Flash Card program.

    This program shows a definition and prompts the user for a "Key Term".
    You also have the option to have the program "remember"
    your answers for a second run through if you would like. 
    This allows you to focus on area's where you need improvement.
    """
    )


def show_menu():
    print(
        """
    Type 'MODE' to change mode.
    Type 'CHAPTERS' to select chapters.
    Type 'START' to begin studying.
    Type 'HELP' to view this menu.
    Type 'DONE' to close the program.
    """
    )


def select_mode(mode):
    # Choose whether to do a single run or multiple runs.
    print()
    selecting = True
    while selecting:
        print(f"You are currently on a {mode} run. ")
        print()
        print(
            'to select or view current setting for whether you would like to do to do one run, a "remembered" run that will omit correct answers from the question pool the the second time around.'
        )
        print()
        change = input("Would you like to change modes (y/n)? ")
        print()
        if change.lower() == "y":
            if mode == "standard":
                mode = "remembered"
            else:
                mode = "standard"
        print(f"You are now on a {mode} run")
        print()
        confirm = input("Would you like to keep this setting (y/n)? ")
        print()
        if confirm.lower() == "y":
            selecting = False
            return mode


def get_chapters():
    # Determine which group of flash cards to draw from to create the test.
    print()
    chapters = list(
        input(
            "Which chapters would you like to study? Input chapter 1, 3, 5, 6 separated with a space. "
        ).split()
    )
    selection = []
    validate = True
    while validate:
        print()
        for item in chapters:
            if item in CHAPTERS_LIST:
                if item not in selection:  # Prevent duplicate values
                    selection.append(item)
                    print(f"Chapter {item} included")
        print()
        answer = input("Does this look correct? (y/n) ")
        if answer.lower() != "y":
            print("All right, we'll try again.")
            selection = []
            chapters = list(
                input(
                    "Which chapters would you like to study? input chapter 1, 3, 5, 6 separated with a space. "
                ).split()
            )
            continue
        else:
            print()
            validate = False
            return selection


def get_user_choice():
    while True:
        choice = input("Enter a menu option: ")
        if choice.upper() in MENU_CHOICES:
            return choice.upper()
        else:
            print("Invalid Choice, please choose again")
            print()


main()
