from playwright.sync_api import sync_playwright, expect
import pytest

from fixtures.browsers import chromium_page
from pages.courses_list_page import CourseListPage
from pages.create_course_page import CreateCoursePage


# @pytest.mark.courses
# @pytest.mark.regression
# def test_empty_courses_list_old():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
#
#         email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#         email_input.fill("user.name@gmail.com")
#
#         username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#         username_input.fill("username")
#
#         password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#         password_input.fill("password")
#
#         registration_button = page.get_by_test_id('registration-page-registration-button')
#         registration_button.click()
#
#         context.storage_state(path='browser-state.json')
#
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(storage_state='browser-state.json')
#         page = context.new_page()
#
#         page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
#
#         courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
#         expect(courses_title).to_be_visible()
#         expect(courses_title).to_have_text('Courses')
#
#         empty_courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
#         expect(empty_courses_icon).to_be_visible()
#
#         empty_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
#         expect(empty_title_text).to_be_visible()
#         expect(empty_title_text).to_have_text('There is no results')
#
#         empty_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
#         expect(empty_description_text).to_be_visible()
#         expect(empty_description_text).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CourseListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_test_create_course(create_course_page: CreateCoursePage, courses_list_page: CourseListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.create_course_toolbar_view.check_visible()
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible(
        title='',
        description='',
        estimated_time='',
        max_score='0',
        min_score='0'
    )

    create_course_page.create_course_exercise_toolbar_view.check_visible()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill(
        title='Playwright',
        description='Playwright',
        estimated_time='2 weeks',
        max_score='100',
        min_score='10'
    )
    create_course_page.create_course_toolbar_view.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title='Playwright',
        max_score='100',
        min_score='10',
        estimated_time='2 weeks'
    )
