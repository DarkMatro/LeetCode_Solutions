def getFolderNames(names: list[str]) -> list[str]:
    """
    ID: 1487
    Tags:   Array, Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an array of strings names of size n. You will create n folders in your file system such
    that, at the ith minute, you will create a folder with the name names[i].

    Since two files cannot have the same name, if you enter a folder name that was previously used,
    the system will have a suffix addition to its name in the form of (k), where, k is the smallest
    positive integer such that the obtained name remains unique.

    Return an array of strings of length n where ans[i] is the actual name the system will assign
    to the ith folder when you create it.

    Parameters
    ----------
    names: list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> getFolderNames(["pes","fifa","gta","pes(2019)"])
    ['pes', 'fifa', 'gta', 'pes(2019)']

    Explanation: Let's see how the file system creates folder names:
    "pes" --> not assigned before, remains "pes"
    "fifa" --> not assigned before, remains "fifa"
    "gta" --> not assigned before, remains "gta"
    "pes(2019)" --> not assigned before, remains "pes(2019)"

    >>> getFolderNames(["gta","gta(1)","gta","avalon"])
    ['gta', 'gta(1)', 'gta(2)', 'avalon']

    Explanation: Let's see how the file system creates folder names:
    "gta" --> not assigned before, remains "gta"
    "gta(1)" --> not assigned before, remains "gta(1)"
    "gta" --> the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
    "avalon" --> not assigned before, remains "avalon"

    >>> getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
    ['onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)', 'onepiece(4)']

    Explanation: When the last folder is created, the smallest positive valid k is 4, and it becomes
    "onepiece(4)".
    """
    name_count = {}  # To track the next suffix for each name
    result = []

    for name in names:
        if name not in name_count:
            # If name is not used, add it to the result
            result.append(name)
            name_count[name] = 1  # Set the next available suffix for this name
        else:
            # If name is already used, find the next available suffix
            k = name_count[name]
            while f"{name}({k})" in name_count:
                k += 1
            # Append the new unique name
            new_name = f"{name}({k})"
            result.append(new_name)
            # Update the map for both the base name and the new name
            name_count[name] = k + 1
            name_count[new_name] = 1  # Start the count for the new name
    return result
