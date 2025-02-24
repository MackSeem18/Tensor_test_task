class ErrorMessages:
    @staticmethod
    def element_is_not_presented(what, where):
        return f'Element {what} is not presented on {where}'

    @staticmethod
    def element_is_not_visible(what, where):
        return f'Element {what} is not visible on {where}'

    @staticmethod
    def cant_click_element(what, where):
        return f'Cant click element {what} on {where}'

    @staticmethod
    def cant_compare_object_locations_and_sizes(what, where):
        return f'Could not compare {what} locations and sizes on {where}.'

    @staticmethod
    def wrong_url(expected_url, actual_url):
        return f'Wrong page URL, expected: {expected_url}, but got {actual_url}'

    @staticmethod
    def elements_parameters_do_not_match(parameter, first_element, second_element, value1, value2):
        return f'Parameters "{parameter}" do not match: {first_element} = {value1}, {second_element} = {value2}'

    @staticmethod
    def region_does_not_match_expected(where, expected_region, actual_region):
        return f'Incorrect region in {where}. Expected: {expected_region}, Actual: {actual_region}'

    @staticmethod
    def actual_file_size_is_different_from_expected(where, file_name, expected_size, actual_size):
        return f'Actual downloaded file {file_name} is different from expected is stated on the page. ' \
               f'Expected: {expected_size}, Actual: {actual_size}'

    @staticmethod
    def timeout_could_not_download_file(file_name, timeout_seconds):
        return f'Timeout! Could not download the file {file_name} in {timeout_seconds} seconds'
