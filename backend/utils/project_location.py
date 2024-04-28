import os

from typing import Final


def check_proj_location() -> str:
    curr_loc: str = os.getcwd()
    new_loc: list[str] = []
    if "vikareta" in curr_loc:
        path_list: list[str] = curr_loc.split("/")
        for loc_item in path_list:
            if not loc_item == "vikareta":
                new_loc.append(loc_item)
            else:
                break
        new_loc.append("vikareta")
        return_loc: str = "/".join(new_loc)
    elif not "vikareta" in curr_loc and "Projects" in curr_loc:
        return_loc: str = f"{curr_loc}/vikareta"
    else:
        proj_path: Final = ["Projects", "vikareta"]
        new_loc: list[str] = ["", "home", curr_loc.split("/")[2]]
        for item in proj_path:
            new_loc.append(item)
        return_loc: str = "/".join(new_loc)
    return return_loc


if __name__ == "__main__":
    check_proj_location()
else:
    pass
