// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "DTrackPlugin/Public/DTrackLiveLinkSourceSettings.h"
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeDTrackLiveLinkSourceSettings() {}

// Begin Cross Module References
DTRACKPLUGIN_API UClass* Z_Construct_UClass_UDTrackLiveLinkSourceSettings();
DTRACKPLUGIN_API UClass* Z_Construct_UClass_UDTrackLiveLinkSourceSettings_NoRegister();
DTRACKPLUGIN_API UEnum* Z_Construct_UEnum_DTrackPlugin_EDTrackCoordinateSystemType();
DTRACKPLUGIN_API UScriptStruct* Z_Construct_UScriptStruct_FDTrackServerSettings();
LIVELINKINTERFACE_API UClass* Z_Construct_UClass_ULiveLinkSourceSettings();
UPackage* Z_Construct_UPackage__Script_DTrackPlugin();
// End Cross Module References

// Begin ScriptStruct FDTrackServerSettings
static FStructRegistrationInfo Z_Registration_Info_UScriptStruct_DTrackServerSettings;
class UScriptStruct* FDTrackServerSettings::StaticStruct()
{
	if (!Z_Registration_Info_UScriptStruct_DTrackServerSettings.OuterSingleton)
	{
		Z_Registration_Info_UScriptStruct_DTrackServerSettings.OuterSingleton = GetStaticStruct(Z_Construct_UScriptStruct_FDTrackServerSettings, (UObject*)Z_Construct_UPackage__Script_DTrackPlugin(), TEXT("DTrackServerSettings"));
	}
	return Z_Registration_Info_UScriptStruct_DTrackServerSettings.OuterSingleton;
}
template<> DTRACKPLUGIN_API UScriptStruct* StaticStruct<FDTrackServerSettings>()
{
	return FDTrackServerSettings::StaticStruct();
}
struct Z_Construct_UScriptStruct_FDTrackServerSettings_Statics
{
#if WITH_METADATA
	static constexpr UECodeGen_Private::FMetaDataPairParam Struct_MetaDataParams[] = {
		{ "BlueprintType", "true" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_m_dtrack_server_port_MetaData[] = {
		{ "Category", "Server Settings" },
		{ "DisplayName", "DTrack Data Port" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
		{ "ToolTip", "Port your server sends data to" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_m_dtrack_start_mea_MetaData[] = {
		{ "Category", "Server Settings" },
		{ "DisplayName", "Start DTrack Measurement" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
		{ "ToolTip", "Start measurement via the DTrack2 TCP command channel" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_m_dtrack_tactile_fingers_MetaData[] = {
		{ "Category", "Server Settings" },
		{ "DisplayName", "Use tactile feedback for fingertracking" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
		{ "ToolTip", "Start DTrack with tactile feedback for fingertracking" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_m_dtrack_server_ip_MetaData[] = {
		{ "Category", "Server Settings" },
		{ "DisplayName", "DTrack Server IP" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
		{ "ToolTip", "IP of DTrack server host for starting measurement" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_m_coordinate_system_MetaData[] = {
		{ "Category", "Server Settings" },
		{ "DisplayName", "DTrack Room Calibration" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
		{ "ToolTip", "Set this according to your DTrack system's room calibration" },
	};
#endif // WITH_METADATA
	static const UECodeGen_Private::FIntPropertyParams NewProp_m_dtrack_server_port;
	static void NewProp_m_dtrack_start_mea_SetBit(void* Obj);
	static const UECodeGen_Private::FBoolPropertyParams NewProp_m_dtrack_start_mea;
	static void NewProp_m_dtrack_tactile_fingers_SetBit(void* Obj);
	static const UECodeGen_Private::FBoolPropertyParams NewProp_m_dtrack_tactile_fingers;
	static const UECodeGen_Private::FStrPropertyParams NewProp_m_dtrack_server_ip;
	static const UECodeGen_Private::FBytePropertyParams NewProp_m_coordinate_system_Underlying;
	static const UECodeGen_Private::FEnumPropertyParams NewProp_m_coordinate_system;
	static const UECodeGen_Private::FPropertyParamsBase* const PropPointers[];
	static void* NewStructOps()
	{
		return (UScriptStruct::ICppStructOps*)new UScriptStruct::TCppStructOps<FDTrackServerSettings>();
	}
	static const UECodeGen_Private::FStructParams StructParams;
};
const UECodeGen_Private::FIntPropertyParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_server_port = { "m_dtrack_server_port", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Int, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FDTrackServerSettings, m_dtrack_server_port), METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_m_dtrack_server_port_MetaData), NewProp_m_dtrack_server_port_MetaData) };
void Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_start_mea_SetBit(void* Obj)
{
	((FDTrackServerSettings*)Obj)->m_dtrack_start_mea = 1;
}
const UECodeGen_Private::FBoolPropertyParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_start_mea = { "m_dtrack_start_mea", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Bool | UECodeGen_Private::EPropertyGenFlags::NativeBool, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, sizeof(bool), sizeof(FDTrackServerSettings), &Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_start_mea_SetBit, METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_m_dtrack_start_mea_MetaData), NewProp_m_dtrack_start_mea_MetaData) };
void Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_tactile_fingers_SetBit(void* Obj)
{
	((FDTrackServerSettings*)Obj)->m_dtrack_tactile_fingers = 1;
}
const UECodeGen_Private::FBoolPropertyParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_tactile_fingers = { "m_dtrack_tactile_fingers", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Bool | UECodeGen_Private::EPropertyGenFlags::NativeBool, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, sizeof(bool), sizeof(FDTrackServerSettings), &Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_tactile_fingers_SetBit, METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_m_dtrack_tactile_fingers_MetaData), NewProp_m_dtrack_tactile_fingers_MetaData) };
const UECodeGen_Private::FStrPropertyParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_server_ip = { "m_dtrack_server_ip", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Str, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FDTrackServerSettings, m_dtrack_server_ip), METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_m_dtrack_server_ip_MetaData), NewProp_m_dtrack_server_ip_MetaData) };
const UECodeGen_Private::FBytePropertyParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_coordinate_system_Underlying = { "UnderlyingType", nullptr, (EPropertyFlags)0x0000000000000000, UECodeGen_Private::EPropertyGenFlags::Byte, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, 0, nullptr, METADATA_PARAMS(0, nullptr) };
const UECodeGen_Private::FEnumPropertyParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_coordinate_system = { "m_coordinate_system", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Enum, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FDTrackServerSettings, m_coordinate_system), Z_Construct_UEnum_DTrackPlugin_EDTrackCoordinateSystemType, METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_m_coordinate_system_MetaData), NewProp_m_coordinate_system_MetaData) }; // 1680811074
const UECodeGen_Private::FPropertyParamsBase* const Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::PropPointers[] = {
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_server_port,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_start_mea,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_tactile_fingers,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_dtrack_server_ip,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_coordinate_system_Underlying,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewProp_m_coordinate_system,
};
static_assert(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::PropPointers) < 2048);
const UECodeGen_Private::FStructParams Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::StructParams = {
	(UObject* (*)())Z_Construct_UPackage__Script_DTrackPlugin,
	nullptr,
	&NewStructOps,
	"DTrackServerSettings",
	Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::PropPointers,
	UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::PropPointers),
	sizeof(FDTrackServerSettings),
	alignof(FDTrackServerSettings),
	RF_Public|RF_Transient|RF_MarkAsNative,
	EStructFlags(0x00000001),
	METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::Struct_MetaDataParams), Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::Struct_MetaDataParams)
};
UScriptStruct* Z_Construct_UScriptStruct_FDTrackServerSettings()
{
	if (!Z_Registration_Info_UScriptStruct_DTrackServerSettings.InnerSingleton)
	{
		UECodeGen_Private::ConstructUScriptStruct(Z_Registration_Info_UScriptStruct_DTrackServerSettings.InnerSingleton, Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::StructParams);
	}
	return Z_Registration_Info_UScriptStruct_DTrackServerSettings.InnerSingleton;
}
// End ScriptStruct FDTrackServerSettings

// Begin Class UDTrackLiveLinkSourceSettings
void UDTrackLiveLinkSourceSettings::StaticRegisterNativesUDTrackLiveLinkSourceSettings()
{
}
IMPLEMENT_CLASS_NO_AUTO_REGISTRATION(UDTrackLiveLinkSourceSettings);
UClass* Z_Construct_UClass_UDTrackLiveLinkSourceSettings_NoRegister()
{
	return UDTrackLiveLinkSourceSettings::StaticClass();
}
struct Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics
{
#if WITH_METADATA
	static constexpr UECodeGen_Private::FMetaDataPairParam Class_MetaDataParams[] = {
		{ "IncludePath", "DTrackLiveLinkSourceSettings.h" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_m_server_settings_MetaData[] = {
		{ "Category", "DTrack settings" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkSourceSettings.h" },
	};
#endif // WITH_METADATA
	static const UECodeGen_Private::FStructPropertyParams NewProp_m_server_settings;
	static const UECodeGen_Private::FPropertyParamsBase* const PropPointers[];
	static UObject* (*const DependentSingletons[])();
	static constexpr FCppClassTypeInfoStatic StaticCppClassTypeInfo = {
		TCppClassTypeTraits<UDTrackLiveLinkSourceSettings>::IsAbstract,
	};
	static const UECodeGen_Private::FClassParams ClassParams;
};
const UECodeGen_Private::FStructPropertyParams Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::NewProp_m_server_settings = { "m_server_settings", nullptr, (EPropertyFlags)0x0010000000000001, UECodeGen_Private::EPropertyGenFlags::Struct, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(UDTrackLiveLinkSourceSettings, m_server_settings), Z_Construct_UScriptStruct_FDTrackServerSettings, METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_m_server_settings_MetaData), NewProp_m_server_settings_MetaData) }; // 1522529015
const UECodeGen_Private::FPropertyParamsBase* const Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::PropPointers[] = {
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::NewProp_m_server_settings,
};
static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::PropPointers) < 2048);
UObject* (*const Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::DependentSingletons[])() = {
	(UObject* (*)())Z_Construct_UClass_ULiveLinkSourceSettings,
	(UObject* (*)())Z_Construct_UPackage__Script_DTrackPlugin,
};
static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::DependentSingletons) < 16);
const UECodeGen_Private::FClassParams Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::ClassParams = {
	&UDTrackLiveLinkSourceSettings::StaticClass,
	nullptr,
	&StaticCppClassTypeInfo,
	DependentSingletons,
	nullptr,
	Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::PropPointers,
	nullptr,
	UE_ARRAY_COUNT(DependentSingletons),
	0,
	UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::PropPointers),
	0,
	0x001000A0u,
	METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::Class_MetaDataParams), Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::Class_MetaDataParams)
};
UClass* Z_Construct_UClass_UDTrackLiveLinkSourceSettings()
{
	if (!Z_Registration_Info_UClass_UDTrackLiveLinkSourceSettings.OuterSingleton)
	{
		UECodeGen_Private::ConstructUClass(Z_Registration_Info_UClass_UDTrackLiveLinkSourceSettings.OuterSingleton, Z_Construct_UClass_UDTrackLiveLinkSourceSettings_Statics::ClassParams);
	}
	return Z_Registration_Info_UClass_UDTrackLiveLinkSourceSettings.OuterSingleton;
}
template<> DTRACKPLUGIN_API UClass* StaticClass<UDTrackLiveLinkSourceSettings>()
{
	return UDTrackLiveLinkSourceSettings::StaticClass();
}
UDTrackLiveLinkSourceSettings::UDTrackLiveLinkSourceSettings() {}
DEFINE_VTABLE_PTR_HELPER_CTOR(UDTrackLiveLinkSourceSettings);
UDTrackLiveLinkSourceSettings::~UDTrackLiveLinkSourceSettings() {}
// End Class UDTrackLiveLinkSourceSettings

// Begin Registration
struct Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkSourceSettings_h_Statics
{
	static constexpr FStructRegisterCompiledInInfo ScriptStructInfo[] = {
		{ FDTrackServerSettings::StaticStruct, Z_Construct_UScriptStruct_FDTrackServerSettings_Statics::NewStructOps, TEXT("DTrackServerSettings"), &Z_Registration_Info_UScriptStruct_DTrackServerSettings, CONSTRUCT_RELOAD_VERSION_INFO(FStructReloadVersionInfo, sizeof(FDTrackServerSettings), 1522529015U) },
	};
	static constexpr FClassRegisterCompiledInInfo ClassInfo[] = {
		{ Z_Construct_UClass_UDTrackLiveLinkSourceSettings, UDTrackLiveLinkSourceSettings::StaticClass, TEXT("UDTrackLiveLinkSourceSettings"), &Z_Registration_Info_UClass_UDTrackLiveLinkSourceSettings, CONSTRUCT_RELOAD_VERSION_INFO(FClassReloadVersionInfo, sizeof(UDTrackLiveLinkSourceSettings), 1945887971U) },
	};
};
static FRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkSourceSettings_h_1842724091(TEXT("/Script/DTrackPlugin"),
	Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkSourceSettings_h_Statics::ClassInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkSourceSettings_h_Statics::ClassInfo),
	Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkSourceSettings_h_Statics::ScriptStructInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkSourceSettings_h_Statics::ScriptStructInfo),
	nullptr, 0);
// End Registration
PRAGMA_ENABLE_DEPRECATION_WARNINGS
