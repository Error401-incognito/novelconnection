
<!-- Drop Down Div -->

<style>
    .dropdown:hover .dropdown-menu {
        display: block;
    }
    summary::marker {
    content: ""; /* Hide the pseudo-element */
    }
</style>

<details >
    <summary>
    <div class="">Reply</div>
    </summary>
    <details-menu role="menu" class="origin-topf-right relative right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
    <div class="pyf-1" role="none">
        <form method="POST" class="p-1 d-flex" action="#" role="none">
            <input type="text"  class="with-border" name="" id="">
            <button type="submit" class="block w-fulfl text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">
            <ion-icon name="send"></ion-icon>
        </button>
        </form>
    </div>
    </details-menu>
</details>





<!-- Reply Comment DIV -->
<div class="flex mr-12" style="margin-right: 20px;">
    <div class="w-10 h-10 rounded-full relative flex-shrink-0">
        <img src="{{request.user.profile.image.url}}" style="width: 40px; height: 40px;" alt="" class="absolute h-full rounded-full w-full">
    </div>
    <div>
        <div class="text-gray-700 py-2 px-3 rounded-md bg-gray-100 relative lg:ml-5 ml-2 lg:mr-12 dark:bg-gray-800 dark:text-gray-100">
            <p class="leading-6">{{c.comment}}</p>
            <div class="absolute w-3 h-3 top-3 -left-1 bg-gray-100 transform rotate-45 dark:bg-gray-800"></div>
        </div>
    </div>
</div>