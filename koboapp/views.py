from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel
import requests

def store_data(request):
    try:
        server = "https://kf.kobotoolbox.org/api/v2/assets"
        form_id = "a5qgk9kEmMB2Wp3foY7zrN"
        KOBO_TOKEN = "393d2a1bb8f790dccc82ed6dbbb0825e0f1a114f"
        url = f"{server}/{form_id}/data.json"
        response = requests.get(url, headers={"Authorization": f"Token {KOBO_TOKEN}"})
        data = response.json()


        for item in data.get('results', []):
 
            
            your_model_instance, created = MyModel.objects.update_or_create(
                _id=item['_id'], 
                defaults={
                'formhub_uuid':item['formhub/uuid'],
                'start' : item['start'],
                'end' : item['end'],
                'Name_of_the_Market':item['Name_of_the_Market'],
                'Name_of_the_person_filling_the_form':item['Name_of_the_person_filling_the_form'],
                'Designation_of_the_person_filling_the_form':item['Designation_of_the_p_son_filling_the_form'],
                'state':item['state'],
                'district':item['district'],
                'City':item['City'],
                'Address_of_Mandi':item['Address_of_Mandi'],
                'Pin_Code':item['Pin_Code'],
                'Year_of_Regulation_under_APMC_act':item.get('Year_of_Regulation_under_APMC_act'),
                'Name_of_Secretary_of_APMC':item.get('Name_of_Secretary_of_APMC'),
                'Mobile_Number':item.get('Mobile_Number'),
                'Email_ID':item.get('Email_ID'),
                'Name_of_Officer_Inch_of_Market_Information':item.get('Name_of_Officer_Inch_f_Market_Information'),
                'Mobile_Number_001':item.get('Mobile_Number_001'),
                'Email_ID_001':item.get('Email_ID_001'),
                'Weekly_Non_working_days':item.get('Weekly_Non_working_days'),
                'Days_of_transaction_in_the_market':item.get('Days_of_transaction_in_the_market'),
                'Type_of_market':item.get('Type_of_market'),
                'Mandi_starting_Time':item.get('Mandi_starting_Time'),
                'Mandi_Closing_Time':item.get('Mandi_Closing_Time'),
                'Number_of_commodities_traded_in_market':item.get('Number_of_commodities_traded_in_market'),
                'Major_Commodities_traded':item.get('Major_Commodities_traded'),
                'Other_major_commodit_ed_in_above_dropdown':item.get('Other_major_commodit_ed_in_above_dropdown'),
                'Are_cold_storage_units_present_in_the_APMC_yard':item.get('Are_cold_storage_uni_ent_in_the_APMC_yard', '').lower() == 'yes',
                'Are_warehouses_present_in_the_APMC_yard':item.get('Are_warehouses_present_in_the_APMC_yard','').lower() == 'yes',
                'Total_number_of_cold_storage_units_in_the_APMC_yard':item.get('Total_number_of_cold_ent_in_the_APMC_yard'),
                'Total_number_of_warehouses_in_the_APMC_yard':item.get('Total_number_of_ware_ent_in_the_APMC_yard'),
                'Total_capacity_of_cold_storage_units_in_Tonnes':item.get('Total_capacity_of_co_APMC_yard_in_Tonnes'),
                'Total_capacity_of_warehouses':item.get('Total_capacity_of_co_APMC_yard'),
                'Does_APMC_market_have_grading_facility':item.get('Does_APMC_market_hav_g_grading_facillity','').lower() == 'yes',
                'Sorting_Grading_capacity_in_tonnes':item.get('Sorting_Grading_capacity_in_tonnes'),
                'Do_you_have_assaying_unit_in_the_market_yard':item.get('Do_you_have_assaying_y_in_the_market_yard','').lower() == 'yes',
                'Does_the_market_have_food_processing_unit':item.get('Does_the_market_have_food_processing_unit','').lower() == 'yes',
                'Number_of_registered_commission_agents':item.get('Number_of_registered_commission_agents'),
                'Number_of_commission_agents':item.get('Number_of_commission_agents'),
                'Revenue_collected_in_Rs':item.get('Revenue_collected_in_Rs'),
                'Revenue_collected_in_Rs_002':item.get('Revenue_collected_in_Rs_002'),
                'Revenue_collected_in_Rs_001':item.get('Revenue_collected_in_Rs_001'),
                'Commodity_wise_type_of_market':item.get('Commodity_wise_type_of_market'),
                'Any_other_category_based_on_commodity':item.get('Any_other_category_based_on_commodity'),
                'Category_of_the_market':item.get('Category_of_the_market'),
                'Define_categories_based_on_fee_collection_Rs':item.get('Define_categories_ba_fee_collection_Rs'),
                'Define_categories_based_on_fee_collection_Rs_001':item.get('Define_categories_ba_fee_collection_Rs_001'),
                'Define_categories_based_on_fee_collection_Rs_002':item.get('Define_categories_ba_fee_collection_Rs_002'),
                'Define_categories_ba_et_fee_collection_Rs_003':item.get('Define_categories_ba_et_fee_collection_Rs_003'),
                'Category_of_the_market_001':item.get('Category_of_the_market_001'),
                'Any_other_category_o_not_specified_above':item.get('Any_other_category_o_not_specified_above'),
                'Total_number_of_villages_served_by_the_market':item.get('Total_number_of_vill_served_by_the_market'),
                'Periodicity_of_functioning_of_market_Start_date':item.get('Periodicity_of_funct_market_Start_date'),
                'Periodicity_of_functioning_of_market_End_date':item.get('Periodicity_of_funct_of_market_End_date'),
                'Any_other_remarks_about_the_periodicity':item.get('Any_other_remarks_about_the_periodicity'),
                'Whether_registered_under_E_NAM':item.get('Whether_registered_under_E_NAM','').lower()=='yes',
                'What_is_the_periodic_enter_0_for_lifetime':item.get('What_is_the_periodic_enter_0_for_lifetime'),
                'What_is_the_license_cified_period_in_Rs':item.get('What_is_the_license_cified_period_in_Rs'),
                'What_is_the_category_of_charge':item.get('What_is_the_category_of_charge'),
                'Any_other_charges_not_specified_above':item.get('Any_other_charges_not_specified_above'),
                'Whether_registered_under_E_NAM_001':item.get('Whether_registered_under_E_NAM_001','').lower()=='yes',
                'Total_number_of_active_yards_in_a_district':item.get('Total_number_of_acti_t_yard_In_a_district'),
                'If_registered_then_year_of_registration':item.get('If_registered_then_year_of_registration'),
                'Availability_of_auction_platforms':item.get('Availability_of_auction_platforms','').lower()=='yes',
                'Capacity_of_auction_platforms_in_Tonnes':item.get('Capacity_of_auction_platform_ln_Tonnes'),
                'Capacity_of_auction_platforms_in_sq_ft':item.get('Capacity_of_auction_platform_ln_sq_ft'),
                'Number_of_auction_platforms':item.get('Number_of_auction_platforms'),
                'What_is_the_daily_auction_starting_time_of_mandi':item.get('What_is_the_daily_au_arting_time_of_mandi'),
                'What_is_the_daily_auction_ending_time_of_mandi':item.get('What_is_the_daily_au_on_end_time_of_mandi'),
                'Does_APMC_market_have_any_expo':item.get('Does_APMC_market_have_any_expo','').lower()=='yes',
                'Export_capacity_in_tonnes':item.get('Export_capacity_In_tonnes'),
                'Does_APMC_market_have_facility_composting_unit':item.get('Does_APMC_market_yar_lity_composing_unit','').lower() == 'yes',
                'Capacity_of_garbage_disposal_unit_in_tonnes':item.get('Capacity_of_garbage_sing_unit_in_tonnes'),
                'Total_No_of_Warehouses_the_market_is_located':item.get('Total_No_of_Warehou_ch_market_is_located'),
                'Do_you_have_any_bank_branch_in_the_market_yard':item.get('Do_you_have_any_bank_y_in_the_market_yard','').lower()=='yes',
                'Do_you_have_any_ATM_in_the_market_yard':item.get('Do_you_have_any_ATM_y_in_the_market_yard','').lower()=='yes',
                'Do_you_have_any_Drinking_Water_facility_in_the_market_yard':item.get('Do_you_have_any_Drin_y_in_the_market_yard','').lower()=='yes',
                'Total_arrival_in_mar_Last_Financial_Year':item.get('Total_arrival_in_mar_Last_Financial_Year'),
                'Total_arrival_in_mar_es_Last_Market_Year':item.get('Total_arrival_in_mar_es_Last_Market_Year'),
                'Total_arrival_in_mar_Last_calendar_Year':item.get('Total_arrival_in_mar_Last_calendar_Year'),
                'Farmers_rest_house_f_lable_in_market_yard':item.get('Farmers_rest_house_f_lable_in_market_yard','').lower()=='yes',
                'Washroom_facility_av_e_in_the_market_yard':item.get('Washroom_facility_av_e_in_the_market_yard','').lower()=='yes',
                'Staff_available_in_t_rket_yard_Permanent':item.get('Staff_available_in_t_rket_yard_Permanent'),
                'What_is_the_daily_da_on_AGMARKNET_portal':item.get('What_is_the_daily_da_on_AGMARKNET_portal'),
                'If_FCM_then_local_name_of_mandi':item.get('If_FCM_then_local_name_of_mandi'),
                'Record_your_current_location':item.get('Record_your_current_location'),
                'Total_volume_traded_value_in_crores_Rs':item.get('Total_volume_traded_value_in_crores_Rs'),
                'version':item.get('__version__'),
                'meta_instanceID':item.get('meta/instanceID'),
                '_xform_id_string':item.get('_xform_id_string'),
                '_uuid':item.get('_uuid'),
                '_attachments':item.get('_attachments'),
                '_status':item.get('_status'),
                '_geolocation':item.get('_geolocation'),
                '_submission_time' : item.get('_submission_time'),
                '_tags':item.get('_tags'),
                '_notes':item.get('_notes'),
                '_validation_status':item.get('_validation_status'),
                '_submitted_by':item.get('_submitted_by')
                }
                
            )
            

        return HttpResponse("Data stored successfully")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)



