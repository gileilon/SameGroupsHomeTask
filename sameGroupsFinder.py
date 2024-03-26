import collections

'''
The program reads from a file named "Groups" and finds identical groups.
Identical groups are groups that have the same elements (duplicates are allowed) with no importance of order.
The text file contains group names and their members to the left.
The program prints a set of sets of names of groups that are identical.
A single group in a set means that the group is unique.
'''


def find_same_groups(file_path):
    # Dictionary: maps elements in a group to a list of group names that contain those elements
    same_groups_dict = collections.defaultdict(list)

    # Parse text file to a data structure dictionary
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.strip().split('(')
            group_name = parts[0].strip()
            elements_str = parts[1][0:len(parts[1]) - 1]
            group_elements = elements_str.strip().split(', ')

            # same_groups_dict : elements in group -> list of group names
            group = tuple(sorted(group_elements))
            if group not in same_groups_dict:  # add group name as value if the group key exist in dict or add a new key
                same_groups_dict[group] = []
            same_groups_dict[group].append(group_name)

        return same_groups_dict


if __name__ == '__main__':
    # make sure 'Groups' file and program file are saved in same directory
    same_groups = find_same_groups(r'Groups.txt')
    print(same_groups.values())










